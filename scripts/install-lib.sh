#!/usr/bin/env bash

set -xeuo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
# --user
pip install --ignore-installed \
  --no-cache-dir --upgrade \
  --upgrade-strategy only-if-needed \
  -r $PROJECT_DIR/requirements.txt
# --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.0.1/constraints-3.7.txt" \
