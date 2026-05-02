# OpenClaw 2026.4.29 Refresh Design

## Goal

Update this `openclaw-ops` skill repo so agent assistants can operate and troubleshoot `openclaw@2026.4.29` without mixing in unreleased `main` or post-0429 behavior.

## Scope

The target release is `2026.4.29`. The npm `latest` and `beta` dist-tags both point to `2026.4.29`, and the installed CLI reports `OpenClaw 2026.4.29 (a448042)`. Live documentation is useful for cross-checking command names and workflows, but the authoritative baseline is the installed CLI plus the local `~/github/openclaw` source and changelog at `2026.4.29`.

## Architecture

Keep the existing skill shape: `skills/openclaw/SKILL.md` remains the routing and quick-reference entry, while `skills/openclaw/references/*.md` holds focused topic references. Add one reference file per missing 2026.4.29 command surface instead of rewriting large existing documents. Update existing references only where the 2026.4.29 changelog changes current advice.

## Files

Create:
- `docs/audits/openclaw-2026.4.29-cli-coverage.md`
- `docs/superpowers/specs/2026-05-02-openclaw-2026-4-29-refresh-design.md`
- `docs/superpowers/plans/2026-05-02-openclaw-2026-4-29-refresh.md`
- `skills/openclaw/references/backup.md`
- `skills/openclaw/references/capability.md`
- `skills/openclaw/references/commitments.md`
- `skills/openclaw/references/devices.md`
- `skills/openclaw/references/directory.md`
- `skills/openclaw/references/dns.md`
- `skills/openclaw/references/mcp.md`
- `skills/openclaw/references/proxy.md`
- `skills/openclaw/references/tasks.md`

Modify:
- `skills/openclaw/SKILL.md`
- `skills/openclaw/references/channels.md`
- `skills/openclaw/references/exec_approvals.md`
- `skills/openclaw/references/memory.md`
- `skills/openclaw/references/providers.md`
- `skills/openclaw/references/queue.md`
- `skills/openclaw/references/security.md`
- `README.md`
- `README_CN.md`
- `.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`

## Data Flow

1. Use npm, installed CLI, local source, and local changelog to pin the target version.
2. Map top-level CLI commands to reference documents.
3. Add missing command references for new or under-documented 2026.4.29 surfaces.
4. Patch existing topic references with release-specific changes.
5. Update README and plugin metadata so distribution surfaces describe the refreshed scope.

## Verification

Run:

```bash
npm_config_cache=/tmp/npm-cache-openclaw-ops npm view openclaw version dist-tags --json
openclaw --version
openclaw --help
git diff --check
```

Then verify coverage with `rg` checks for the 2026.4.29 command names across `skills/openclaw/SKILL.md` and `skills/openclaw/references`.

## Non-Goals

- Do not import `2026.5.x` or GitHub `main`-only behavior into the baseline.
- Do not change OpenClaw runtime config or local service state.
- Do not refactor the skill into a different plugin layout.
