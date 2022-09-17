#!/bin/bash

set -xe
set -o pipefail

IMAGE=$1
TAG=$2

docker run --rm $IMAGE:$TAG venv/bin/flask test

exit 0
