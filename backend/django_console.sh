source variables.sh

echo "Run Docker Django console Exit with CONTROL+A+D"

docker-compose -p $DOCKER_NAME exec $SERVICE_NAME screen -r django