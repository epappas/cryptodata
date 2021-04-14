#!/usr/bin/env bash

set -xeo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

export COMPOSE_FILE=${PROJECT_DIR}/docker-compose.yaml
exec docker-compose run airflow db upgrade
