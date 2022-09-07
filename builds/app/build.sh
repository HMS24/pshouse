#!/bin/bash

# exit when any command failed
set -xe
set -o pipefail

# declare
DOCKERFILE_DIR_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# build docker image
docker buildx build \
--no-cache \
--platform linux/amd64 \
-t $WEB_IMAGE:$WEB_TAG \
-f $DOCKERFILE_DIR_PATH/Dockerfile .

exit 0
