#!/usr/bin/env bash

source ./common.sh

changeToProjectRoot

rm -rf dist build
rm -rf ./pyenv-3.12.8/lib/python3.12/site-packages/easy-install.pth
rm -rf ./pyenv-3.12.8/bin/buildlackey
rm -rf ./pyenv-3.12.8/lib/python3.12/site-packages/easy-install.pth
rm -rf ./pyenv-3.12.8/bin/unittests
rm -rf ./pyenv-3.12.8/bin/runtests
rm -rf ./pyenv-3.12.8/bin/runmypy
rm -rf ./pyenv-3.12.8/bin/prodpush
rm -rf ./pyenv-3.12.8/bin/cleanup
rm -rf ./pyenv-3.12.8/bin/package

find . -type d -name '*'.egg-info -delete
find . -type f -name "*.log"      -delete

rm -rf .eggs
rm -rf buildlackey.egg-info

# to uninstall in developer mode -- pip uninstall pyut2xml
