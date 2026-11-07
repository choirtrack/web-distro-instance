FROM mariadb:10.4

# https://www.drupal.org/forum/support/before-you-start/2018-12-12/mysql-or-mariadb#comment-12947135

ADD sql/ /docker-entrypoint-initdb.d

RUN apt-get update && apt-get -y install vim

EXPOSE 3306

CMD ["mysqld"]


# latest mariadb or mysql version

# set any environment variables

