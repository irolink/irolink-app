#!/usr/bin/env sh
pkill -KILL uwsgi
echo '' > /var/log/uwsgi/irolink-app.log
uwsgi --ini ./src/config/uwsgi-local-web.ini --py-autoreload 1
