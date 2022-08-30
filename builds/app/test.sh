#!/bin/bash

set -xe
set -o pipefail

IMAGE="pshouse:latest"

docker run --rm $IMAGE venv/bin/flask test

exit 0
