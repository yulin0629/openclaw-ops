# Command Queue

> Source: https://docs.openclaw.ai/concepts/queue

## Why

Auto-reply runs can be expensive (LLM calls) and collide when multiple inbound messages arrive simultaneously. Serialization prevents competing for shared resources (session files, logs, CLI stdin) and reduces upstream rate limits.

## How It Works

- Lane-aware FIFO queue drains each lane with configurable concurrency cap
- Default concurrency: unconfigured lanes = 1, `main` = 4, `subagent` = 8
- `runEmbeddedPiAgent` enqueues by session key (lane `session:<key>`) — only one active run per session
- Each session run queues into global lane (`main`) — capped by `agents.defaults.maxConcurrent`
- Typing indicators fire immediately on enqueue (when channel-supported)
- Additional lanes (`cron`, `subagent`) allow background jobs to execute without blocking inbound replies

## Queue Modes (Per Channel)

| Mode | Behavior |
|---|---|
| `steer` | Default for active-run queueing in 2026.4.29. Drain pending steering messages into the active Pi run at the next model/tool boundary. Falls back to followup if the run cannot be steered. |
| `followup` | Enqueue for the next agent turn after the current run ends. |
| `collect` | Coalesce all queued messages into a single followup turn; messages targeting different channels/threads drain individually. |
| `steer-backlog` | Steer now and preserve the message for a followup turn. |
| `interrupt` (legacy) | Abort the active run for that session, then run the newest message. |
| `queue` (legacy) | Preserve the older one-at-a-time steering behavior. |

## Queue Options

| Option | Description | Default |
|---|---|---|
| `debounceMs` | Wait for quiet before starting followup turn | `1000` |
| `cap` | Max queued messages per session | `20` |
| `drop` | Overflow policy: `old`, `new`, `summarize` | `summarize` |

`summarize` keeps a short bullet list of dropped messages and injects it as a synthetic followup prompt.

2026.4.29 defaults active-run queueing to `steer` with a 500ms followup fallback debounce. Older examples may still show `collect`; use `collect` only when you want queued messages coalesced into the next separate turn.

## Configuration

```json5
{
  messages: {
    queue: {
      mode: "steer",
      debounceMs: 500,
      cap: 20,
      drop: "summarize",
      byChannel: {
        discord: "collect",
        whatsapp: "collect",
      },
    },
  },
}
```

## Per-Session Overrides

```
/queue <mode>                              # Set mode for current session
/queue collect debounce:2s cap:25 drop:summarize  # Combine options
/queue default                             # Clear override
/queue reset                               # Clear override
```

## Scope & Guarantees

- Applies to auto-reply agent runs across all inbound channels
- Default lane (`main`) is process-wide for inbound + main heartbeats
- Per-session lanes guarantee only one agent run per session simultaneously
- Pure TypeScript + promises — no external dependencies or worker threads

## Troubleshooting

- Enable verbose logs; search for `"queued for ...ms"` lines
- If runs pile up, check `agents.defaults.maxConcurrent` setting
- For high-volume channels, consider `collect` mode with higher `debounceMs`
