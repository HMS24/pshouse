#!/bin/bash

# exit when any command failed
set -xe
set -o pipefail

# declare
DOCKERFILE_DIR_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
IMAGE="pshouse:latest"
GUNICORN_OPTIONS="--reload"

# build docker image
docker build \
--build-arg GUNICORN_OPTIONS=$GUNICORN_OPTIONS \
-t $IMAGE \
-f $DOCKERFILE_DIR_PATH/Dockerfile .

exit 0
