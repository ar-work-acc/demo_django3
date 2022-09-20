#!/bin/bash
# for local development: docker compose
docker compose up -d --build && docker image prune -f
docker container ls -a
