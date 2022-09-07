#!/bin/bash

set -xe
set -o pipefail

# login
docker login -u $DOCKER_USER --password-stdin < ~/docker_pass

# tag
docker tag $WEB_IMAGE:$WEB_TAG $DOCKER_USER/$WEB_IMAGE:$WEB_TAG

# push
docker push $DOCKER_USER/$WEB_IMAGE:$WEB_TAG

exit 0
