#!/usr/bin/env bash

source ./common.sh

changeToProjectRoot

mypy --config-file .mypi.ini --pretty --no-color-output --show-error-codes --check-untyped-defs   src/buildlackey tests

status=$?

echo "Exit with status: ${status}"
cd -
exit ${status}

