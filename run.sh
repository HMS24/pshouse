#!/bin/bash

set -e
set -o pipefail

USER=$1
HOST=$2

echo "**********************************"
echo "** Building image ****************"
echo "**********************************"

builds/app/build.sh

echo "**********************************"
echo "** Testing ***********************"
echo "**********************************"

builds/app/test.sh

echo "**********************************"
echo "** Pushing image *****************"
echo "**********************************"

builds/app/push.sh

echo "**********************************"
echo "** Deploying *********************"
echo "**********************************"

deploy/deploy.sh $USER $HOST

# docker compose up -d
exit 0