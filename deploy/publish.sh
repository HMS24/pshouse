#!/bin/bash

set -e
set -o pipefail

export IMAGE=$(sed -n '1p' /tmp/.auth)
export TAG=$(sed -n '2p' /tmp/.auth)
export DOCKER_USER=$(sed -n '3p' /tmp/.auth)
export PROXY_IMAGE=$(sed -n '4p' /tmp/.auth)
export PROXY_IMAGE_TAG=$(sed -n '5p' /tmp/.auth)
DOCKER_PASS=$(sed -n '6p' /tmp/.auth)

rm /tmp/.auth

echo "$DOCKER_PASS" > docker login -u $DOCKER_USER --password-stdin

cd ~/psh && docker compose up -d

exit 0