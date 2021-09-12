#!/usr/bin/env bash

set -xeuo pipefail

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

exec docker-compose \
  -f ${PROJECT_DIR}/docker-compose.yaml \
  down --volumes --rmi all --remove-orphans
