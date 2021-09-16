#!/usr/bin/env bash

set -euo pipefail

export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

if [ $# -eq 0 ]; then
  >&2 echo "set a tap name to execute"
  exit 1
elif [ $# -eq 2 ] && [ "${2}" == "discover" ]; then
  exec tap-"${1}" -c $PROJECT_DIR/data/config."${1}".json --discover
else
  exec tap-"${1}" \
    --config $PROJECT_DIR/data/config."${1}".json \
    --properties $PROJECT_DIR/data/properties."${1}".json \
    --catalog $PROJECT_DIR/data/properties."${1}".json \
    --state $PROJECT_DIR/data/state."${1}".json \
    | while read -r entry; do
      case "${entry}" in
        *"\"type\": \"RECORD\""*) echo "RECORD=>${entry}";;
        *"\"type\": \"SCHEMA\""*) echo "SCHEMA=>${entry}";;
        *"\"type\": \"STATE\""*) echo "STATE=>${entry}";;
        *"\"type\": \"ACTIVATE_VERSION\""*) echo "ACTIVATE_VERSION=>${entry}";;
        # *) echo "UKNOWN=>${entry}";;
      esac
    done
fi
