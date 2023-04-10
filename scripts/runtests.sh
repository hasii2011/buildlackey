#!/usr/bin/env bash

source ./common.sh

changeToProjectRoot

python3 -m tests.buildlackey.commands.TestRunTests
status=$?
checkStatus ${status} TestRunTests

python3 -Wdefault -m tests.TestAll
status=$?

cd - > /dev/null 2>&1  || ! echo "No such directory"

echo "Exit with status: ${status}"
exit "${status}"
