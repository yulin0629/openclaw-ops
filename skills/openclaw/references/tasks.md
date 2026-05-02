# Tasks Reference

Target release: OpenClaw 2026.4.29.

`openclaw tasks` inspects durable background task state and TaskFlow state. Use it for subagent, ACP, cron, CLI, and maintenance diagnostics when work is queued, stuck, lost, or completed in the background.

## Commands

```bash
openclaw tasks list
openclaw tasks list --runtime subagent
openclaw tasks list --status running
openclaw tasks show <taskId-or-runId-or-sessionKey>
openclaw tasks cancel <taskId>
openclaw tasks audit
openclaw tasks maintenance
openclaw tasks maintenance --help
openclaw tasks notify <taskId> done_only
openclaw tasks notify <taskId> state_changes
openclaw tasks notify <taskId> silent
openclaw tasks flow list
openclaw tasks flow show <flowId>
openclaw tasks flow cancel <flowId>
```

## Filters

| Option | Values |
|---|---|
| `--runtime <name>` | `subagent`, `acp`, `cron`, `cli` |
| `--status <name>` | `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled`, `lost` |
| `--json` | Machine-readable output |

Notify policies: `done_only`, `state_changes`, `silent`.

## When To Use

- A spawned subagent or ACP run appears stuck.
- Cron jobs are queued or not reporting completion.
- A task says it succeeded but the user did not see the expected message.
- `doctor` reports stale sessions or background task inconsistencies.
- You need to cancel a long-running background task.

## 2026.4.29 Maintenance Notes

- Task maintenance reconciles stale background tasks and TaskFlow state.
- Orphaned subagent sessions can be bounded and recovered instead of requiring manual `sessions.json` surgery.
- `doctor` can surface maintenance actions; inspect with `tasks audit` before applying broader repair flows.

## Triage Ladder

```bash
openclaw tasks list --status running
openclaw tasks audit
openclaw tasks show <id>
openclaw logs --follow
openclaw doctor
```

## Related References

- [subagents.md](subagents.md) — nested spawned sessions
- [acp_agents.md](acp_agents.md) — external ACP runtimes
- [automation.md](automation.md) — cron and webhooks
- [sessions.md](sessions.md) — stored session lifecycle
