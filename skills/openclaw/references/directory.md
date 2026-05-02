# Directory Reference

Target release: OpenClaw 2026.4.29.

`openclaw directory` looks up contact, peer, group, and account IDs for supported chat channels. Use it when configuring allowlists, default targets, group routing, or message delivery targets.

## Commands

```bash
openclaw directory self --channel slack
openclaw directory peers list --channel slack --query "alice"
openclaw directory peers list --channel telegram --limit 20 --json
openclaw directory groups list --channel discord
openclaw directory groups members --channel discord --group-id <id>
```

## Subcommands

| Command | Purpose |
|---|---|
| `self` | Show the connected account identity |
| `peers list` | List or search contacts/users |
| `groups list` | List groups/channels |
| `groups members` | List members for a specific group |

## Common Options

| Option | Use |
|---|---|
| `--channel <name>` | Channel, auto-selected when only one is configured |
| `--account <id>` | Specific channel account ID |
| `--query <text>` | Search query for peers |
| `--limit <n>` | Limit results |
| `--json` | Machine-readable output |

## When To Use

- Building `allowFrom` lists with exact channel IDs.
- Finding Discord/Slack channel IDs for message delivery.
- Checking which account OpenClaw is currently using for a channel.
- Auditing group membership before enabling broad group permissions.

## Related References

- [channels.md](channels.md) — channel setup
- [channel_routing.md](channel_routing.md) — session keys and routing
- [security.md](security.md) — allowlists and access control
