#!/bin/bash
export PROJECT_DIR=django_project
export DOCKER_PROJECT_DIR=django_docker
export DOCKER_NAME=django_project_template
export SERVICE_NAME=django_project_template
for l in $(cat .env-db.yaml); do export "$l"; done
for l in $(cat .env-api.yaml); do export "$l"; done
for l in $(cat .env-common.yaml); do export "$l"; done
for l in $(cat .env-redis.yaml); do export "$l"; done
for l in $(cat .env-memcache.yaml); do export "$l"; done
for l in $(cat .env-nginx.yaml); do export "$l"; done