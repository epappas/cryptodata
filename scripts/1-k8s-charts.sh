#!/usr/bin/env bash

set -xeuo pipefail

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
export NAMESPACE="${NAMESPACE:-airflow}"

helm repo add "stable" "https://charts.helm.sh/stable" --force-update
helm repo add airflow-stable https://airflow-helm.github.io/charts
helm repo add superset https://apache.github.io/superset
helm repo add bitnami https://charts.bitnami.com/bitnami


# get latest list of changes
helm repo update
