#!/bin/bash

set -xe
set -o pipefail

# login
docker login -u $DOCKER_USER --password-stdin < ~/docker_pass

# tag
docker tag $IMAGE $DOCKER_USER/$IMAGE

# push
docker push $DOCKER_USER/$IMAGE

exit 0
