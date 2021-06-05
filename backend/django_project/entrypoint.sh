#!/bin/bash

timeout=0
isReady=0
if [ "$DATABASE_TYPE" = "pg" ]
then
    echo "Waiting for postgres..."
    while ! isReady; do
      echo "Not ready"
        if [ $timeout -le $TIMEOUT]
        then
            waittime=$((waittime+1))
            sleep 10;
            isReady = $(pg_isready --port $PGPORT --host=$PGHOST);
        else
            isReady=1
        fi
    done
    echo "PostgreSQL started"
fi


echo "Starting Django"
python manage.py makemigrations accounts
python manage.py makemigrations
python manage.py migrate


if test -f "initial_data/accounts.json"; then
    python manage.py loaddata initial_data/accounts.json --ignorenonexistent
fi


if test -f "initial_data/sites.json"; then
    python manage.py loaddata initial_data/sites.json --ignorenonexistent
fi


if test -f "initial_data/flatpages.json"; then
    python manage.py loaddata initial_data/flatpages.json --ignorenonexistent
fi


screen -wipe
screen -dmS queue celery -b redis://$REDIS_HOST:6379 -A project worker -B -E
screen -dmS django gunicorn project.wsgi:application --bind 0.0.0.0:8001 --proxy-protocol --strip-header-spaces

echo "Django Started"
tail -f /var/log/lastlog
exec "$@"
