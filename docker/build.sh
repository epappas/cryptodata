#!/usr/bin/env bash

set -xeuo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

export COMPOSE_FILE=${PROJECT_DIR}/docker-compose.yaml
if [ $# -eq 0 ]; then
  exec docker-compose build
else
  exec docker-compose build "${@- }"
fi
