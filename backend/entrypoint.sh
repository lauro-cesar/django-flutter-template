#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 10
    done

    echo "PostgreSQL started"
fi
sleep 20
python manage.py makemigrations accounts --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
# celery -A project worker -B -S django --scheduler django_celery_beat.schedulers:DatabaseScheduler
exec "$@"
