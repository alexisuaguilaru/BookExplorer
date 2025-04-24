#!/bin/sh

envsubst '$DOMAIN_NAME' < /etc/nginx/conf.d/nginx.conf.template > /etc/nginx/conf.d/default.conf

chown -R $UID:$GID /etc/nginx

exec gosu $UID:$GID nginx -g 'daemon off;'