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
# --since and --until
# git log -S"config.menu_items"
# git log --grep="JRA-224:"
# git log --author="John\|Mary"
# git whatchanged --since="2 weeks ago"
exec git log --format=format: --name-only -- $PROJECT_DIR | egrep -v '^$' | sort | uniq -c | sort -r
