#!/bin/bash

set -xe
set -o pipefail

DOCKER_USER="chimei24"
DOCKER_PASS=$1
IMAGE="pshouse:latest"

# login
docker login -u $DOCKER_USER -p $DOCKER_PASS

# tag
docker tag $IMAGE $DOCKER_USER/$IMAGE

# push
docker push $DOCKER_USER/$IMAGE

exit 0
