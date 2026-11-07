# config export process for public distro

Based on: https://drupal.stackexchange.com/a/308680/1082

At top level folder for git:

`cd config/sync`
`find . -type f -exec sed -i -e '/_core:/,+1d' {} \;`
`find . -type f -exec sed -i -e '/uuid: /d' {} \;`

Then:
 
`git add .` 
`git commit -m "config"`

---

**Note (2026-11-07):** this recipe is for a future install profile's
`config/install` directory, where uuids must not be present. `config/sync` in
this repository is a normal `drush cex` of the running instance and keeps its
uuids, because `drush cim` needs them to update existing configuration.
