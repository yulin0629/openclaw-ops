# Commitments Reference

Target release: OpenClaw 2026.4.29.

Commitments are opt-in inferred follow-up reminders. OpenClaw can extract likely follow-ups from conversations, scope them by agent/channel, and deliver due reminders through heartbeat.

## Commands

```bash
openclaw commitments
openclaw commitments list
openclaw commitments --all
openclaw commitments --agent work
openclaw commitments --status pending
openclaw commitments --json
openclaw commitments dismiss cm_abc123
```

## Options

| Option | Use |
|---|---|
| `--agent <id>` | Inspect one agent |
| `--all` | Show all statuses |
| `--status <status>` | `pending`, `sent`, `dismissed`, `snoozed`, `expired` |
| `--json` | Machine-readable output |

## Config

Minimal opt-in:

```json5
{
  commitments: {
    enabled: true,
    maxPerDay: 5,
  },
}
```

## Behavior In 2026.4.29

- Extraction is hidden/batched so normal replies are not polluted with reminder bookkeeping.
- Commitments are scoped by agent and channel where applicable.
- Heartbeat delivery wakes can surface due reminders.
- Due times are clamped to the heartbeat interval so reminders do not immediately echo after extraction.

## Operations

- Start with a small `maxPerDay` until the agent's extraction quality is acceptable.
- Use `openclaw commitments --all` during tuning to see dismissed, sent, snoozed, and expired entries.
- Use `openclaw commitments dismiss <id>` for false positives.
- If reminders are not delivered, check heartbeat first: `openclaw system heartbeat last`.

## Related References

- [heartbeat.md](heartbeat.md) — heartbeat delivery and agent check-ins
- [automation.md](automation.md) — scheduled jobs and webhooks
- [tasks.md](tasks.md) — durable task state and maintenance
