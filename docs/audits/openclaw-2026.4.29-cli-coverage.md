# OpenClaw 2026.4.29 CLI Coverage Audit

Audit date: 2026-05-02

## Version Baseline

| Source | Evidence |
|---|---|
| npm registry | `npm view openclaw version dist-tags --json` reports `latest: 2026.4.29` and `beta: 2026.4.29` |
| Installed CLI | `openclaw --version` reports `OpenClaw 2026.4.29 (a448042)` |
| Local source | `~/github/openclaw/package.json` reports `2026.4.29`; latest local commit is `a448042c2e` |
| Changelog | `~/github/openclaw/CHANGELOG.md` contains the target `2026.4.29` release notes |

Live `main` documentation can contain content newer than this target release. Treat it as a cross-check only unless it matches the installed CLI or local `2026.4.29` source.

## 2026.4.29 Coverage Matrix

| CLI surface | Current coverage before refresh | Refresh action |
|---|---|---|
| `acp` | Covered by `acp_agents.md` | Keep and link from `SKILL.md` |
| `agent`, `agents` | Covered by `multi_agent.md` and `agent_runtime.md` | Keep; add newer task/subagent routing notes where relevant |
| `approvals` | Covered by `exec_approvals.md` | Update with `exec-policy` relationship |
| `backup` | Missing dedicated reference | Add `backup.md` |
| `capability`, `infer` | Missing dedicated reference | Add `capability.md` |
| `channels` | Covered by `channels.md` and troubleshooting | Update with 2026.4.29 channel-change notes |
| `commitments` | Missing dedicated reference | Add `commitments.md` |
| `config`, `configure`, `onboard`, `setup` | Covered by `config_reference.md`, `install.md`, `SKILL.md` | Keep; add config keys for commitments/visible replies |
| `cron` | Covered by `automation.md` | Keep; link with `tasks.md` |
| `devices` | Mentioned in `nodes.md` only | Add `devices.md`; keep `nodes.md` for runtime node capabilities |
| `directory` | Missing dedicated reference | Add `directory.md` |
| `dns` | Partial via Bonjour/presence docs | Add `dns.md` |
| `docs` | Mentioned in `SKILL.md` | Keep |
| `exec-policy` | Missing dedicated reference | Update `exec_approvals.md` and quick reference |
| `gateway`, `daemon`, `health`, `logs`, `status` | Covered by gateway refs | Keep; add task maintenance diagnostics |
| `hooks`, `webhooks` | Covered by `hooks.md` and `automation.md` | Keep |
| `mcp` | Slash-command MCP mentioned only | Add `mcp.md` |
| `memory` | Covered | Update with people wiki, Active Memory filters, partial recall, REM preview |
| `message` | Covered by channel and media docs | Keep; add visible replies note |
| `models` | Covered by `providers.md` and `model_failover.md` | Update NVIDIA and Codex/OpenAI-compatible notes |
| `node`, `nodes`, `pairing`, `qr` | Covered by node/pairing refs | Keep; split device token/pairing operations into `devices.md` |
| `plugins`, `skills`, `clawhub` | Covered | Keep |
| `proxy` | Missing dedicated reference | Add `proxy.md` |
| `sandbox` | Covered by `sandboxing.md` | Keep |
| `secrets`, `security` | Covered | Update policy notes for 2026.4.29 |
| `sessions` | Covered | Link task/subagent recovery notes |
| `system` | Covered by presence/heartbeat refs | Keep |
| `tasks` | Missing dedicated reference | Add `tasks.md` |
| `tui`, `chat`, `terminal` | Covered by `tui.md` | Keep |
| `update`, `uninstall`, `reset` | Covered by `install.md` | Keep |

## 2026.4.29 Release Themes To Reflect

- Messaging defaults: active-run queueing defaults to `steer`, with followup fallback debounce.
- Reply visibility: `messages.visibleReplies` can require visible replies through `message(action=send)`.
- Commitments: opt-in inferred follow-ups can be extracted and delivered through heartbeat.
- Tasks: task maintenance reconciles stale background tasks, TaskFlows, and orphaned subagent sessions.
- Memory: people-aware wiki, provenance views, Active Memory chat filters, partial recall on timeout, and REM preview diagnostics.
- Providers: NVIDIA provider onboarding/catalogs, Bedrock Opus 4.7 thinking parity, and safer Codex/OpenAI-compatible streaming/replay behavior.
- Security/ops: configured `tools.exec` and `tools.fs` no longer widen restricted tool profiles implicitly; use explicit `alsoAllow`.
- Channels: Slack, Telegram, Discord, WhatsApp, Signal, Microsoft Teams, Matrix, Feishu, QQBot, and Yuanbao changes should be summarized at reference level.
