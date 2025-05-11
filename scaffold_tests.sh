#!/usr/bin/env bash
set -e

# List your Django apps here
apps=(
  accounts
  pages
  blog
  store
  portfolio
)

for app in "${apps[@]}"; do
  dir="$app/tests"
  mkdir -p "$dir"
  file="$dir/test_models.py"
  if [ ! -f "$file" ]; then
    # Capitalize first letter of app name
    first="$(echo "${app:0:1}" | tr '[:lower:]' '[:upper:]')"
    rest="${app:1}"
    className="${first}${rest}ModelsSmokeTest"

    cat > "$file" <<EOF
from django.test import TestCase

class ${className}(TestCase):
    def test_smoke(self):
        # trivial test to verify ${app} app loads
        self.assertTrue(True)
EOF
    echo "Created $file"
  else
    echo "Skipped $file (already exists)"
  fi
done
