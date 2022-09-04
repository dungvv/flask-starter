#!/usr/bin/env bash
set -e

use_tag="fetek-io/flask-starter"

docker build -t "$use_tag" .