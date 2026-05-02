# Backup Reference

Target release: OpenClaw 2026.4.29.

`openclaw backup` creates and verifies local archives for OpenClaw config, credentials, sessions, and workspaces. Use it before upgrades, migrations, risky config changes, and machine moves.

## Commands

```bash
openclaw backup create
openclaw backup create --output ~/Backups
openclaw backup create --dry-run --json
openclaw backup create --verify
openclaw backup create --no-include-workspace
openclaw backup create --only-config
openclaw backup verify ./2026-03-09T00-00-00.000Z-openclaw-backup.tar.gz
openclaw backup verify ~/Backups/latest.tar.gz --json
```

## Create Options

| Option | Use |
|---|---|
| `--output <path>` | Archive path or destination directory |
| `--dry-run` | Print the backup plan without writing an archive |
| `--json` | Machine-readable output |
| `--verify` | Validate the archive immediately after writing |
| `--no-include-workspace` | Exclude workspace directories |
| `--only-config` | Back up only the active JSON config file |

## What To Back Up Before

- `openclaw update` or `npm install -g openclaw@latest`
- `openclaw doctor --fix` on a heavily customized install
- edits to `~/.openclaw/openclaw.json`
- moving to a new Mac/Linux/Windows host
- changing channel credentials or multi-agent routing

## Operational Notes

- Prefer `openclaw backup create --verify` for upgrade checkpoints.
- Use `--dry-run --json` when automation needs to inspect what will be archived.
- Use `--only-config` for small config snapshots before a direct config edit.
- Use `--no-include-workspace` when workspaces are large or already backed up by git.
- Always run `openclaw backup verify <archive>` before treating an archive as restorable.

## Related References

- [install.md](install.md) — update, rollback, migration, uninstall
- [config_reference.md](config_reference.md) — config file shape
- [security.md](security.md) — local state and credential handling
