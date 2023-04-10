#!/usr/bin/env bash

source ./common.sh

changeToProjectRoot

rm -rf dist build
rm -rf ./pyenv-3.10.0/lib/python3.10/site-packages/easy-install.pth
rm -rf ./pyenv-3.10.0/bin/buildlackey

find . -type d -name '*'.egg-info -delete
find . -type f -name "*.log"      -delete

rm -rf .eggs
rm -rf buildlackey.egg-info

# to uninstall in developer mode -- pip uninstall pyut2xml
