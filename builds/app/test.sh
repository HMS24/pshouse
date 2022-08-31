#!/bin/bash

set -xe
set -o pipefail

docker run --rm $IMAGE venv/bin/flask test

exit 0
