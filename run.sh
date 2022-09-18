#!/bin/bash -e

set -o pipefail

# declare
TARGET=""
SSH_PEM=""
DOCKER_USER="local"
DOCKER_PASS=""
IMAGE="psh"
TAG="latest"
PROXY_IMAGE="proxy"
PROXY_IMAGE_TAG="latest"

while [[ "$#" -gt 0 ]]; do
	case $1 in
		--target) TARGET="$2"; shift ;;
		--ssh-pem) SSH_PEM="$2"; shift ;;
		--docker-user) DOCKER_USER="$2"; shift ;;
		--docker-pass) DOCKER_PASS="$2"; shift ;;
		--image) IMAGE="$2"; shift ;;
		--tag) TAG="$2"; shift ;;
		*) echo "Unknown parameter passed: $1"; exit 1 ;;
	esac
	shift
done

if [ -z "$TARGET" ]; then
	echo "--target argument is required!"
	exit 1
fi

if [ "$TARGET" != "local" ] && [ -z "$SSH_PEM" ]; then
	echo "--ssh-pem argument is required!"
	exit 1
fi

if [ "$TARGET" != "local" ] && [ "$DOCKER_USER" == "local" ]; then
	echo "--docker-user argument is required!"
	exit 1
fi

if [ "$TARGET" != "local" ] && [ -z "$DOCKER_PASS" ]; then
	echo "--docker-pass argument is required!"
	exit 1
fi

# build
echo "**********************************"
echo "** Building image ****************"
echo "**********************************"

builds/build.sh "app" $IMAGE $TAG
builds/build.sh "proxy" $PROXY_IMAGE $PROXY_IMAGE_TAG

# test
echo "**********************************"
echo "** Testing ***********************"
echo "**********************************"

builds/app/test.sh $IMAGE $TAG

# push
echo "**********************************"
echo "** Pushing image *****************"
echo "**********************************"

builds/push.sh \
$TARGET \
$IMAGE \
$TAG \
$DOCKER_USER \
$DOCKER_PASS

builds/push.sh \
$TARGET \
$PROXY_IMAGE \
$PROXY_IMAGE_TAG \
$DOCKER_USER \
$DOCKER_PASS

# deploy
echo "**********************************"
echo "** Deploying *********************"
echo "**********************************"

echo "Deploy to $TARGET"

if [ "$TARGET" = "local" ]; then
	DOCKER_USER=$DOCKER_USER \
	PROXY_IMAGE=$PROXY_IMAGE \
	PROXY_IMAGE_TAG=$PROXY_IMAGE_TAG \
	IMAGE=$IMAGE \
	TAG=$TAG \
	docker compose up -d

else
    deploy/deploy.sh \
	$TARGET \
	$SSH_PEM \
	$IMAGE \
	$TAG \
	$DOCKER_USER \
	$DOCKER_PASS \
	$PROXY_IMAGE \
	$PROXY_IMAGE_TAG
fi

exit 0
