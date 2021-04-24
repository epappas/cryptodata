#!/usr/bin/env bash

set -xeuo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

source $PROJECT_DIR/.venv/bin/activate

pip install --upgrade --upgrade-strategy only-if-needed \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.0.1/constraints-3.7.txt" \
  "apache-airflow==2.0.1"

pip install --upgrade --upgrade-strategy only-if-needed \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.0.1/constraints-3.7.txt" \
  -r $PROJECT_DIR/requirements-dev.txt

pip install --upgrade --upgrade-strategy only-if-needed \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.0.1/constraints-3.7.txt" \
  -r $PROJECT_DIR/requirements.txt
