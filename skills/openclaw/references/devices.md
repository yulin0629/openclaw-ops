# Devices Reference

Target release: OpenClaw 2026.4.29.

`openclaw devices` manages device pairing requests and device auth tokens. It is the pairing/token surface; use [nodes.md](nodes.md) for runtime node capabilities such as camera, screen, location, and node exec.

## Commands

```bash
openclaw devices list
openclaw devices approve <requestId>
openclaw devices approve --latest
openclaw devices reject <requestId>
openclaw devices remove <deviceId>
openclaw devices clear
openclaw devices rotate --device <id> --role <role>
openclaw devices revoke --device <id> --role <role>
```

## Pairing Flow

1. Start or connect a node/device.
2. Inspect pending requests:
   ```bash
   openclaw devices list
   ```
3. Approve the specific request:
   ```bash
   openclaw devices approve <requestId>
   ```
4. Verify runtime presence:
   ```bash
   openclaw nodes status
   openclaw system presence
   ```

## Approval Options

| Option | Use |
|---|---|
| `--latest` | Show/approve the most recent pending request explicitly |
| `--url <url>` | Gateway WebSocket URL |
| `--token <token>` | Gateway token |
| `--password <password>` | Gateway password |
| `--timeout <ms>` | Approval timeout |
| `--json` | Machine-readable output |

Token rotation/revocation uses `--device <id>` and `--role <role>`. `rotate` can also attach one or more `--scope <scope>` values.

## Device Versus Node

| Concept | CLI | Purpose |
|---|---|---|
| Device auth/pairing | `openclaw devices` | Pending approvals, paired device entries, role tokens |
| Node runtime | `openclaw node`, `openclaw nodes` | Node host service and paired node capabilities |

## Operations

- Prefer approving explicit `requestId` values over broad approval habits.
- Rotate device tokens after suspected token exposure or host migration.
- Use `remove` for a single stale device and `clear` only when rebuilding the device table.
- Node exec is still governed by exec approvals on the node host.

## Related References

- [nodes.md](nodes.md) — node runtime capabilities
- [pairing.md](pairing.md) — gateway-owned node pairing
- [exec_approvals.md](exec_approvals.md) — node exec approvals
- [security.md](security.md) — gateway and node trust boundaries
