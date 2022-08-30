#!/bin/bash

set -e
set -o pipefail

# build
echo "********** Building Docker Image **********"
builds/app/build.sh

# test
echo "********** Testing **********"
builds/app/test.sh

# push
echo "********** Pushing Docker Image **********"
builds/app/push.sh $DOCKER_PASS

# deploy
echo "********** Deploying **********"
docker compose up -d

exit 0