#!/usr/bin/env bash
# Rebuilds downloads/*.zip from each plugin's skill folders, so people on the
# Claude app can upload a skill without zipping anything themselves.
# Each ZIP has the skill folder as its root, which is what the upload expects.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -f downloads/*.zip
for dir in */skills/*/; do
  name="$(basename "$dir")"
  (cd "$(dirname "$dir")" && zip -qr -X "$OLDPWD/downloads/$name.zip" "$name" -x '*.DS_Store')
done
ls -1 downloads/
