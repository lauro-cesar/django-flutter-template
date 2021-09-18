#!/bin/bash
source variables.sh

echo "Run Docker"
docker-compose -p $DOCKER_NAME up
