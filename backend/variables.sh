#!/bin/bash
for l in $(cat .env-project.yaml); do export "$l"; done
for l in $(cat .env-db.yaml); do export "$l"; done
for l in $(cat .env-api.yaml); do export "$l"; done
for l in $(cat .env-common.yaml); do export "$l"; done
for l in $(cat .env-redis.yaml); do export "$l"; done
for l in $(cat .env-memcache.yaml); do export "$l"; done
for l in $(cat .env-nginx.yaml); do export "$l"; done