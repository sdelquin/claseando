#!/bin/bash

docker run -p 8080:80 -e "ERRORS=1" -v $PWD/imw:/var/www/html/ richarvey/nginx-php-fpm
