#!/usr/bin/env bash

set -xeuo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

if [ $# -eq 0 ]; then
  >&2 echo "set a service to run"
  exit 1
else
  exec docker-compose \
  -f ${PROJECT_DIR}/docker-compose.yaml \
  -f ${PROJECT_DIR}/docker-compose.airflow.yaml \
  -f ${PROJECT_DIR}/docker-compose.superset.yaml \
  run --rm "${@}"
fi
