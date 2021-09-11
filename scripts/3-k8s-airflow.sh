#!/usr/bin/env bash

set -xeuo pipefail

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
export NAMESPACE="${NAMESPACE:-airflow}"

# install airflow helm chart
# we use https://helm.sh/docs/topics/advanced/#post-rendering
helm install \
airflow \
airflow-stable/airflow \
--version 7.16.0 \
--namespace "${NAMESPACE}" \
--values "${PROJECT_DIR}/airflow-setup.yaml" \
--values "${PROJECT_DIR}/airflow-secrets.yaml" \
--post-renderer "${PROJECT_DIR}/scripts/envsubst.sh"

kubectl get deployments
kubectl get pods
