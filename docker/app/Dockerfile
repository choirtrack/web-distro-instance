FROM php:7.3-fpm
# do i need a linux docker image to start with?
# how can we assume it's ubuntu/debian with apt-get

# assumes some already installed

# but you can also start with php with an operating system
#FROM php:fpm-alpine
# so what does FROM php:7.3-fpm have in it as an OS
# and why does FROM php:fpm-alpine not specify a version of php?

# drupal 8.6.4 now supports 7.3 so we're good

# do all this as docker user

# add extensions
RUN apt-get install -y \
    git \
    zip \
    curl \
    sudo \
    unzip
# TODO: how can we assume it's ubuntu/debian with apt-get

# assumes some already installed
#
# required extensions include:
# cli (built in)
# intl (This dockerfile)
# xml (built in)
# simplexml (This dockerfile)
# mbstring (built in)
# gd (This dockerfile)
# curl (built in)
# soap (This dockerfile)

RUN docker-php-ext-install \
    cli \
    intl \ 
    xml \ 
    simplexml \
    mbstring \ 
    gd \ 
    curl \ 
    soap \ 
    zip

RUN {  \
		echo "memory_limit = 1024M"; \
	} >> /usr/local/etc/php/php.ini

# install composer

# fpm setup?

#        pear: {  }
#        pecl: {  }
#    ini:
#        display_errors: 'On'
#        error_reporting: '-1'
#        session.save_path: /var/lib/php/session
#        date.timezone: UTC
#    fpm_ini:
#        error_log: /var/log/php-fpm.log
#    fpm_pools:
#        pool1:
#            ini:
#                prefix: www
#                listen: '127.0.0.1:9000'
#                security.limit_extensions: .php
#                user: www-user
#                group: www-data
#    composer: '1'
#    composer_home: ''




# php-fpm
# select php version - 7.x



# set environment variables
# php memory limit


#Install Drush 8.1.2
RUN wget https://github.com/drush-ops/drush/releases/download/8.1.2/drush.phar && php drush.phar core-status && chmod +x drush.phar \
	&& mv drush.phar /usr/local/bin/drush

#Install Drupal Console
RUN curl http://drupalconsole.com/installer -L -o drupal.phar
RUN mv drupal.phar /usr/local/bin/drupal && chmod +x /usr/local/bin/drupal
RUN drupal init
