#!/usr/bin/env bash

set -xeuo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

export COMPOSE_FILE=${PROJECT_DIR}/docker-compose.yaml
if [ $# -eq 0 ]; then
  >&2 echo "set a service to connect to"
  exit 1
else
  exec docker-compose exec "${@}" /bin/bash
fi
