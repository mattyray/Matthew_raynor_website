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
  # Ensure the tests/ directory exists
  mkdir -p "$dir"
  file="$dir/test_models.py"
  # Only write if the file doesn't already exist
  if [ ! -f "$file" ]; then
    cat > "$file" <<EOF
from django.test import TestCase

class ${app^}ModelsSmokeTest(TestCase):
    def test_smoke(self):
        # trivial test to verify ${app} app loads
        self.assertTrue(True)
EOF
    echo "Created $file"
  else
    echo "Skipped $file (already exists)"
  fi
done
