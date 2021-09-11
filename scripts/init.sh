#!/usr/bin/env bash

set -xeuo pipefail

helm plugin install https://github.com/zendesk/helm-secrets

# On mac, if you are missing gpg
# brew install gpg
