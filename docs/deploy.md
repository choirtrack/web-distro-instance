# Deploying ligc.choirtrack.net to server 04

The site runs on Rob's DigitalOcean droplet "server 04" (SSH alias
`server04`, 104.248.164.167) in the layout of the
[provision-site toolkit](https://github.com/therobyouknow/infrastructure/tree/main/provision-site/toolkit):
`/var/www/09/ligc.choirtrack.net/{releases/<version>/code, deployment_environments/live, settings/1, backups, logs}`.
The toolkit commands (`create_release`, `deploy`, `drush_run`, `backup_db`,
`restore_db`, `update_symlink`, `site_status`) are on the server's PATH.

Secrets (database password, Gmail SMTP app password, hash salt) live only on
the server in `settings/1/settings.local.php`.

## One-off server preparation (done 2026-11-07)

Site structure, database `dligcchoirtrack_1`, `settings/1/settings.local.php`
(copied from server02 with new database credentials and a new hash salt), the
Apache vhost `ligc.choirtrack.net.conf` with the Let's Encrypt certificate
copied from server02, and a `drush cron` crontab entry every 30 minutes.
Release 1.0.0 = branch `feat/drupal-11-server04` (Drupal 11.4.12). The database
is the server02 dump of 2026-11-07 upgraded in ddev (10.1.7 → 10.6.21, Tour
uninstalled while it still existed, → 11.4.12) and then restored on server04;
restoring the raw Drupal 10 dump into the Drupal 11 code fails in
`search_update_11401` because core 11 no longer ships Tour. Both dumps are
kept in `backups/database/` on the server.

## Releasing a new version

```sh
# local: merge to main, tag, push both remotes
git tag -a v1.0.1 -m "1.0.1"
git push origin main --tags
git push drupal main:2.0.x --tags

# server: clone the tag into a new release, link settings and files, deploy
ssh server04
create_release ligc.choirtrack.net 1.0.1 https://github.com/choirtrack/web-distro-instance.git v1.0.1
cd /var/www/09/ligc.choirtrack.net/releases/1.0.1/code/web/sites/default
ln -sfn ../../../../../../settings/1/settings.local.php settings.local.php
ln -sfn ../../../../../../deployment_environments/live/assets/public/files files
deploy ligc.choirtrack.net live 1.0.1      # backup_db, composer install, symlink flip, php-fpm reload, updb, cr
drush_run ligc.choirtrack.net live "cim -y"
drush_run ligc.choirtrack.net live "core:requirements --severity=1"
```

`create_release` links `settings/2` by default; this site uses database 1,
hence the first `ln`. Rollback: `update_symlink ligc.choirtrack.net live <previous>`,
then `sudo systemctl reload php8.5-fpm` and `drush_run ligc.choirtrack.net live cr`;
restore the pre-deploy dump with `restore_db` if `updb` changed anything.

## Content and files

Content is edited on the server. To work on it locally:

```sh
fetch_and_import_env_db.sh server04 ligc.choirtrack.net live   # from the toolkit
sync_files.sh server04 ligc.choirtrack.net live pull
```

## DNS and certificate

`ligc.choirtrack.net` has a 30 s TTL A record. To cut over, point it at
104.248.164.167. The vhost already serves the certificate copied from
server02 (valid to 2026-12-24); once DNS has moved, put renewal on server04:

```sh
sudo certbot --apache -d ligc.choirtrack.net
```

which issues a fresh certificate and rewrites the vhost to use it. Until the
DNS change the site answers only to requests carrying the host name:
`curl -k --resolve ligc.choirtrack.net:443:104.248.164.167 https://ligc.choirtrack.net/user/login`.
