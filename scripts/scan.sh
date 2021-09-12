#!/usr/bin/env bash

set -xeuo pipefail

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

if [ $# -eq 0 ]; then
  exec docker-compose \
  -f ${PROJECT_DIR}/docker-compose.yaml \
  scan
else
  exec docker-compose \
  -f ${PROJECT_DIR}/docker-compose.yaml \
  scan "${@- }"
fi
