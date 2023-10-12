#!/usr/bin/env bash

source ./common.sh

changeToProjectRoot

rm -rf dist build
rm -rf ./pyenv-3.11.0/lib/python3.11/site-packages/easy-install.pth
rm -rf ./pyenv-3.11.0/bin/buildlackey
rm -rf ./pyenv-3.11.0/lib/python3.11/site-packages/easy-install.pth
rm -rf ./pyenv-3.11.0/bin/unittests
rm -rf ./pyenv-3.11.0/bin/runtests
rm -rf ./pyenv-3.11.0/bin/runmypy
rm -rf ./pyenv-3.11.0/bin/prodpush
rm -rf ./pyenv-3.11.0/bin/cleanup
rm -rf ./pyenv-3.11.0/bin/package

find . -type d -name '*'.egg-info -delete
find . -type f -name "*.log"      -delete

rm -rf .eggs
rm -rf buildlackey.egg-info

# to uninstall in developer mode -- pip uninstall pyut2xml
