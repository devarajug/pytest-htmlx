#!/usr/bin/env bash
set -euo pipefail

PACKAGE_NAME="pytest-htmlx"

echo "📦 Building $PACKAGE_NAME ..."

# Clean old builds
rm -rf dist/ build/ *.egg-info

# Build (source + wheel)
python -m build

echo "🚀 Uploading to TestPyPI ..."

twine upload \
  --repository-url https://test.pypi.org/legacy/ \
  -u __token__ \
  -p "$TEST_PYPI_API_TOKEN" \
  dist/*

echo "✅ Uploaded to TestPyPI!"
echo "🔍 Verify install with:"
echo "pip install --index-url https://test.pypi.org/simple/ --no-deps $PACKAGE_NAME"
