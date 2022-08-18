#!/bin/bash

# exit when any command failed
set -xe
set -o pipefail

# declare
DOCKERFILE_DIR_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ -z "$FLASK_CONFIG" ]; then
	echo "FLASK_CONFIG argument is required!"
	exit 1
fi

# build docker image
docker build \
-t presale:latest \
-f $DOCKERFILE_DIR_PATH/Dockerfile .

exit 0
