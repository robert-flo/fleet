# Sync personal fork (ADR 0024)

Reusable workflow: `sync-personal-fork.yml`, invoked with `workflow_call` from another repo. Cadence is the caller's job (Omarchy: cron `0 10 * * *` = 04:00 America/El_Salvador).

## What it does

1. Fast-forwards the fork’s mirror branch (`upstream` by default) from `upstream_repo` / `upstream_branch`.
2. Rebases `personal` onto that mirror.
3. On success: pushes the mirror (regular) and `personal` (`--force-with-lease`).
4. On conflict: `git rebase --abort`, opens or comments an issue titled `[Conflicto Rebase]…`, does not push.

No package build (Omarchy-only). Do not add a skills or Omarchy caller in this repo.

## Thin caller

```yaml
name: Sync personal fork
on:
  schedule:
    - cron: "0 10 * * *"
  workflow_dispatch:
jobs:
  sync:
    uses: robert-flo/fleet/.github/workflows/sync-personal-fork.yml@main
    with:
      upstream_repo: mattpocock/skills
      upstream_branch: main
      # mirror_branch: upstream
      # personal_branch: personal
    permissions:
      contents: write
      issues: write
    secrets: inherit
```

Optional secret `token`: a PAT when `GITHUB_TOKEN` cannot push protected `personal`.

## Access

`robert-flo/fleet` is private. Under **Settings → Actions → General → Access**, allow other `robert-flo` repositories to use workflows from fleet, or callers cannot `uses:` this file.
