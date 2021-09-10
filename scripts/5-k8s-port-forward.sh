#!/usr/bin/env bash

set -xeuo pipefail

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
export NAMESPACE="${NAMESPACE:-airflow}"

# View the airflow UI webserver in your browser. Click on the URL based within this terminal output
# view airflow UI
export POD_NAME=$(kubectl get pods --namespace "${NAMESPACE}" -l "component=web,app=airflow" -o jsonpath="{.items[0].metadata.name}")

echo "airflow UI webserver --> http://127.0.0.1:8080"

kubectl port-forward --namespace "${NAMESPACE}" "${POD_NAME}" 8080:8080
