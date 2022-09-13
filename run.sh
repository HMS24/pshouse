#!/bin/bash

set -e
set -o pipefail

DEPLOY_PLACE=$1

# replace ??????
export DOCKER_USER=?????? && export WEB_IMAGE=?????? && export WEB_TAG=??????

if [ -z "$DEPLOY_PLACE" ]; then
	echo "DEPLOY_PLACE argument is required!"
	exit 1
fi

# build
echo "**********************************"
echo "** Building image ****************"
echo "**********************************"

builds/app/build.sh

# test
echo "**********************************"
echo "** Testing ***********************"
echo "**********************************"

builds/app/test.sh

# push
echo "**********************************"
echo "** Pushing image *****************"
echo "**********************************"

builds/app/push.sh

# deploy
echo "**********************************"
echo "** Deploying *********************"
echo "**********************************"

if [ "$USER" = "localhost" ]; 
    then
        echo "Deploy to localhost"
        docker compose up -d
    else
        echo "Deploy to $DEPLOY_PLACE"
        deploy/deploy.sh $DEPLOY_PLACE
fi

exit 0