#!/bin/bash

set -e
set -o pipefail

export WEB_IMAGE=$(sed -n '1p' /tmp/.auth)
export WEB_TAG=$(sed -n '2p' /tmp/.auth)
export DOCKER_USER=$(sed -n '3p' /tmp/.auth)
export DOCKER_PASS=$(sed -n '4p' /tmp/.auth)

echo "$DOCKER_PASS" > docker login -u $DOCKER_USER --password-stdin

cd ~/psh && docker compose up -d && rm /tmp/.auth 

exit 0