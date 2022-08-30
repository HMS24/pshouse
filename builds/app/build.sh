#!/bin/bash

# exit when any command failed
set -xe
set -o pipefail

# declare
DOCKERFILE_DIR_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
IMAGE="pshouse:latest"

# build docker image
docker build \
 --no-cache \
-t $IMAGE \
-f $DOCKERFILE_DIR_PATH/Dockerfile .

exit 0
