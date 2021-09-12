#!/usr/bin/env bash

set -xeuo pipefail

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

if [ $# -eq 0 ]; then
  exec docker-compose \
  -f ${PROJECT_DIR}/docker-compose.yaml \
  pull --include-deps --ignore-pull-failures
else
  exec docker-compose \
  -f ${PROJECT_DIR}/docker-compose.yaml \
  pull --include-deps --ignore-pull-failures "${@- }"
fi
