#!/usr/bin/env bash

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
export NAMESPACE="${NAMESPACE:-airflow}"

# delete helm deployment
helm delete airflow
helm delete superset

# remove anything running on port 8080 and 8001 for lingering airflow webserver deployment
# lsof -i:8080 -i:8001 -Fp | sed 's/^p//' | xargs kill -9

set +e
# delete secrets for smoother setup if someone needs to change the service account
kubectl delete namespace "${NAMESPACE}"
set -e
