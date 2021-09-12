#!/usr/bin/env bash

set -xeuo pipefail

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
export NAMESPACE="${NAMESPACE:-airflow}"

# View the airflow UI webserver in your browser. Click on the URL based within this terminal output
# view airflow UI
export POD_NAME=$(kubectl get pods --namespace "${NAMESPACE}" -l "app=postgresql" -o jsonpath="{.items[0].metadata.name}")

kubectl port-forward --namespace "${NAMESPACE}" "${POD_NAME}" 5432:5432
