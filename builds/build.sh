#!/bin/bash

# exit when any command failed
set -xe
set -o pipefail

# declare
SERVICE=$1
IMAGE=$2
TAG=$3
DOCKERFILE_DIR_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# build docker image
docker buildx build \
--platform linux/amd64 \
-t $IMAGE:$TAG \
-f $DOCKERFILE_DIR_PATH/$SERVICE/Dockerfile .

exit 0
