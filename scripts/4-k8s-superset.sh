#!/usr/bin/env bash

set -xeuo pipefail

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
export NAMESPACE="${NAMESPACE:-airflow}"

# install superset helm chart
# we use https://helm.sh/docs/topics/advanced/#post-rendering
helm install \
superset \
superset/superset \
--version 0.1.1 \
--namespace "${NAMESPACE}" \
--values "${PROJECT_DIR}/superset-setup.yaml" \
--post-renderer "${PROJECT_DIR}/scripts/envsubst.sh" \

kubectl get deployments
kubectl get pods
