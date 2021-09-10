#!/usr/bin/env bash

set -xeuo pipefail

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
export NAMESPACE="${NAMESPACE:-airflow}"


# load kube config into local git repo
# https://www.astronomer.io/docs/cli-kubepodoperator/#run-your-container
mkdir -p "${PROJECT_DIR}/.kube/" && cat "${HOME}/.kube/config" > "${PROJECT_DIR}/.kube/config"
