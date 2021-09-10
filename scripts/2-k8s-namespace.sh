#!/usr/bin/env bash

set -xeuo pipefail

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
export NAMESPACE="${NAMESPACE:-airflow}"

# export PARENT_DIR="$(dirname `pwd`)"
kubectl create namespace "${NAMESPACE}"

# check if it's created
kubectl get namespaces

# swtich to airflow namespace
kubectl config set-context $(kubectl config current-context) --namespace="${NAMESPACE}"
kubectl config view | grep namespace
kubectl get pods

