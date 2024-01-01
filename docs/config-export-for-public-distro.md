# config export process for public distro

Based on: https://drupal.stackexchange.com/a/308680/1082

At top level folder for git:

`cd config/sync`
`find . -type f -exec sed -i -e '/_core:/,+1d' {} \;`
`find . -type f -exec sed -i -e '/uuid: /d' {} \;`

Then:
 
`git add .` 
`git commit -m "config"`
