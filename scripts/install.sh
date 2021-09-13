#!/usr/bin/env bash

set -xeuo pipefail

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

pip install --ignore-installed \                                                         
  --no-cache-dir --upgrade \
  --upgrade-strategy only-if-needed \
  -r "${PROJECT_DIR}/requirements.txt"
