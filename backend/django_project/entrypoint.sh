#!/bin/bash

timeout=0
isReady=0

if [ -z ${DATABASE_PORT} ] ; then
    until nc -z ${DATABASE_HOST} ${DATABASE_PORT}; do
    echo "$(date) - waiting for database"
    sleep 5
done
fi

echo "Starting Django"
python manage.py makemigrations accounts checklists --noinput
python manage.py migrate --noinput


if test -f "initial_data/accounts.json"; then
    python manage.py loaddata initial_data/accounts.json 
fi


if test -f "initial_data/sites.json"; then
    python manage.py loaddata initial_data/sites.json --ignorenonexistent
fi


if test -f "initial_data/flatpages.json"; then
    python manage.py loaddata initial_data/flatpages.json --ignorenonexistent
fi


screen -wipe
screen -dmS queue celery -b redis://$REDIS_HOST:$REDIS_PORT/$REDIS_DB -A project worker -B -E -Q $REDIS_QUEUE_NAME
screen -dmS django gunicorn project.wsgi:application --bind 0.0.0.0:8001 --proxy-protocol --strip-header-spaces

echo "Django Started"
tail -f /var/log/lastlog
exec "$@"
