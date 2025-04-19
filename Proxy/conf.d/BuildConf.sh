#!/bin/sh

envsubst '$DOMAIN_NAME' < /etc/nginx/conf.d/nginx.conf.template > /etc/nginx/conf.d/default.conf

cat /etc/nginx/conf.d/nginx.conf

exec nginx -g 'daemon off;'