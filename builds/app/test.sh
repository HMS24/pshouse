#!/bin/bash

set -xe
set -o pipefail

docker run --rm $IMAGE:$TAG venv/bin/flask test

exit 0
