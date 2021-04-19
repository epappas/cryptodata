#!/usr/bin/env bash

set -xeuo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

if [ $# -eq 0 ]; then
  exec docker-compose \
  -f ${PROJECT_DIR}/docker-compose.yaml \
  -f ${PROJECT_DIR}/docker-compose.airflow.yaml \
  -f ${PROJECT_DIR}/docker-compose.superset.yaml \
  build
else
  exec docker-compose \
  -f ${PROJECT_DIR}/docker-compose.yaml \
  -f ${PROJECT_DIR}/docker-compose.airflow.yaml \
  -f ${PROJECT_DIR}/docker-compose.superset.yaml \
  build "${@- }"
fi
