#!/bin/bash
source variables.sh

echo "Build Docker"
docker-compose -p $DOCKER_NAME build