#!/usr/bin/env bash

set -xeuo pipefail

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
export NAMESPACE="${NAMESPACE:-airflow}"

envsubst '${PROJECT_DIR}' <&0
