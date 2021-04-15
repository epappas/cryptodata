#!/usr/bin/env bash

set -xeuo pipefail

pip install --ignore-installed \
  --no-cache-dir --upgrade \
  --upgrade-strategy only-if-needed \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.0.1/constraints-3.7.txt" \
  "apache-airflow==2.0.1"
