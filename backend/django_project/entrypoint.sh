#!/bin/bash

if [ "$DATABASE_TYPE" = "pg" ]
then
    echo "Waiting for postgres..."
    while ! pg_isready --port $PGPORT --host=$PGHOST; do
      echo "Not ready"
      sleep 10
    done
    echo "PostgreSQL started"
fi


echo "Starting Django"
python manage.py makemigrations accounts app_settings app_users sites flatpages
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput



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
