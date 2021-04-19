#!/usr/bin/env bash

set -xeuo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

if [ $# -eq 0 ]; then
  >&2 echo "set a tap name to execute"
  exit 1
elif [ $# -eq 2 ] && [ "${2}" == "discover" ]; then
  exec tap-"${1}" -c $PROJECT_DIR/data/config."${1}".json --discover
else
  exec tap-"${1}" \
    -c $PROJECT_DIR/data/config."${1}".json \
    -p $PROJECT_DIR/data/properties."${1}".json \
    -s $PROJECT_DIR/data/state."${1}".json
fi
