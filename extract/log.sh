#!/usr/bin/env bash
# Count how many times the file has changed

set -euo pipefail

PROJECT_DIR="$(cd "${1-.}" && pwd)"
if [ ! -d "$PROJECT_DIR" ]; then
  >&2 echo "$PROJECT_DIR is not a directory path"
  exit 1
fi

cd $PROJECT_DIR

# --after=2016-01-01
# --before=2016-01-01
exec git log --all --numstat --date=short --pretty=format:'--%h--%ad--%aN' --no-renames
