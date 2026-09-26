#!/usr/bin/env bash
# Idempotent bootstrap for the OpenMS Hugo website in a Cloud Agent environment.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Keep the pinned Hugo version aligned with netlify.toml.
HUGO_VERSION="$(sed -nE 's/.*HUGO_VERSION[[:space:]]*=[[:space:]]*"([^"]+)".*/\1/p' netlify.toml | head -1)"
HUGO_VERSION="${HUGO_VERSION:-0.155.0}"

install_hugo() {
  local tmpdir
  tmpdir="$(mktemp -d)"
  local url="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz"
  echo "Installing Hugo extended ${HUGO_VERSION} ..."
  curl -sSL -o "${tmpdir}/hugo.tar.gz" "$url"
  tar -xzf "${tmpdir}/hugo.tar.gz" -C "$tmpdir"
  sudo mv "${tmpdir}/hugo" /usr/local/bin/hugo
  rm -rf "$tmpdir"
}

# Install Hugo only if missing or the wrong version (must be the extended build).
if ! command -v hugo >/dev/null 2>&1; then
  install_hugo
elif ! hugo version | grep -q "v${HUGO_VERSION}.*extended"; then
  install_hugo
else
  echo "Hugo extended ${HUGO_VERSION} already present."
fi

hugo version

# Fetch the scientific-python-hugo-theme submodule.
git submodule update --init --recursive
