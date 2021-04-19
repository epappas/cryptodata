#!/usr/bin/env bash

set -xeuo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

exec docker-compose \
  -f ${PROJECT_DIR}/docker-compose.yaml \
  -f ${PROJECT_DIR}/docker-compose.superset.yaml \
  up -d
