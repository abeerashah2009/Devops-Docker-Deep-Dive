#!/bin/bash
# Minimal local CI: build -> test -> deploy
set -e

echo "== BUILD =="
docker compose build

echo "== TEST =="
docker compose up --abort-on-container-exit --exit-code-from test test redis

docker compose down -v

echo "== DEPLOY =="
docker compose up -d web
