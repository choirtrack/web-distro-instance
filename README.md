# ChoirTrack – web distro instance

ChoirTrack is a Drupal 11 site for running a choir's repertoire: songs with
part recordings and scores, set lists, rehearsal weeks, workshops and a
dashboard. It is free and open source (GPL-2.0-or-later). The first instance
is https://ligc.choirtrack.net.

## One codebase, two remotes

| Remote   | URL                                                   | Branch          |
|----------|-------------------------------------------------------|-----------------|
| `origin` | git@github.com:choirtrack/web-distro-instance.git     | `main` (issues, PRs) |
| `drupal` | git@git.drupal.org:project/choirtrack.git             | `2.0.x` (drupal.org release branch) |

Develop against `origin`; after merging to `main`, mirror it to drupal.org:

```sh
git push drupal main:2.0.x
```

The drupal.org release branch is `2.0.x` (Drupal 11). The earlier `1.0.x` branch holds the
pre-rewrite Drupal 10 history and is being retired; its removal was requested from the
Drupal.org webmasters because a branch with a dev release cannot be force-pushed or deleted
by maintainers.

The drupal.org history (two 2024 commits) was merged into this repository on
2026-11-07, so both remotes share one history from then on.

## Local development (ddev)

```sh
ddev start
ddev composer install
ddev import-db --file=path/to/dump.sql.gz      # or fetch_and_import_env_db.sh
ddev drush cim -y && ddev drush cr
ddev drush uli
```

Put local overrides in `web/sites/default/settings.local.php` (ignored by
git); the hard-coded database block and hash salt were removed from
`settings.php` in November 2026. On a server, the toolkit links
`settings/<n>/settings.local.php` into the release.

## Configuration

`config/sync` is a full `drush cex` of the instance, with uuids. The
uuid-stripping recipe in `docs/config-export-for-public-distro.md` is for a
future install profile's `config/install`, not for this directory.

## Deployment

See `docs/deploy.md` for the server04 release procedure.
