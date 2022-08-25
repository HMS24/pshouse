#!/bin/bash

set -e
set -o pipefail

# build
echo "********** Building Docker Image **********"
docker compose build app proxy

# test
echo "********** Testing **********"
flask test

# deploy
echo "********** Deploying **********"
docker compose up -d

exit 0