#!/bin/bash
source variables.sh
docker stop "${DOCKER_NAME}_pg"
docker rm "${DOCKER_NAME}_pg"
docker create --name "${DOCKER_NAME}_pg" -e POSTGRES_USER=$PGUSER  -e POSTGRES_PASSWORD=$PGPASSWORD -e POSTGRES_DB=$PGDATABASE -p $PGHOSTADDR:$PGPORT:5432 postgis/postgis:12-2.5-alpine
docker start "${DOCKER_NAME}_pg"