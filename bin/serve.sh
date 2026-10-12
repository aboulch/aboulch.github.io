#!/usr/bin/env bash
# Launch the local Jekyll dev server (http://localhost:4000/).
# Usage: bin/serve.sh [extra jekyll serve args, e.g. --port 4001]
set -euo pipefail

cd "$(dirname "$0")/.."

export RBENV_VERSION=3.3.7
export BUNDLE_PATH="$HOME/bundle-alfolio-33"

# Linuxbrew's ld shadows the system linker and breaks native gem builds.
PATH=$(echo "$PATH" | tr ':' '\n' | grep -v linuxbrew | paste -sd:)
export PATH

exec bundle exec jekyll serve --livereload "$@"
