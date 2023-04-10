#!/bin/bash

source ./common.sh

changeToProjectRoot

clear

python3 -m build --sdist --wheel

#  pip install -e .  to host locally

# Check package
twine check dist/*
