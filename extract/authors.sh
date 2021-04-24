#!/usr/bin/env bash

set -euo pipefail

PROJECT_DIR="$(cd "${1-.}" && pwd)"
if [ ! -d "$PROJECT_DIR" ]; then
  >&2 echo "$PROJECT_DIR is not a directory path"
  exit 1
fi

cd $PROJECT_DIR

exec git log \
  --all --numstat --date=short \
  --pretty=format:"--%h--%ad--%aN" \
  --no-renames -- $PROJECT_DIR
