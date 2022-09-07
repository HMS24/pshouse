#!/bin/bash

set -xe
set -o pipefail

docker run --rm $WEB_IMAGE:$WEB_TAG venv/bin/flask test

exit 0
