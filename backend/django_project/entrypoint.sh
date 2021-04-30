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
python manage.py makemigrations accounts arquivos sites flatpages
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput


# python manage.py inspectdb tb_user > arquivos/models/tb_user.py
# python manage.py inspectdb tb_acquirer > arquivos/models/tb_acquirer.py
# python manage.py inspectdb tb_core_acquirer > arquivos/models/tb_core_acquirer.py
# python manage.py inspectdb tb_core_layout > arquivos/models/tb_core_layout.py
# python manage.py inspectdb tb_core_van > arquivos/models/tb_core_van.py
# python manage.py inspectdb tb_core_file_origin > arquivos/models/tb_core_file_origin.py
# python manage.py inspectdb tb_core_file_origin_client > arquivos/models/tb_core_file_origin_client.py


if test -f "initial_data.json"; then
    python manage.py loaddata initial_data.json --ignorenonexistent
fi

if test -f "auth.json"; then
    python manage.py loaddata auth.json --ignorenonexistent
fi

screen -wipe
screen -dmS queue celery -b redis://$REDIS_HOST:6379 -A project worker -B -E
screen -dmS django gunicorn project.wsgi:application --bind 0.0.0.0:8001 --proxy-protocol --strip-header-spaces

echo "Django Started"
tail -f /var/log/lastlog
exec "$@"
