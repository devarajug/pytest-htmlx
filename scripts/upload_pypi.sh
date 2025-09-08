#!/usr/bin/env bash
set -euo pipefail

PACKAGE_NAME="pytest-htmlx"

echo "📦 Building $PACKAGE_NAME ..."

# Clean old builds
rm -rf dist/ build/ *.egg-info

# Build (source + wheel)
python -m build

echo "🚀 Uploading to PyPI ..."

twine upload \
  -u __token__ \
  -p "$PYPI_API_TOKEN" \
  dist/*

echo "✅ Uploaded to PyPI!"
