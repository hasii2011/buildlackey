#!/bin/bash

source ./common.sh

changeToProjectRoot

clear

twine upload  dist/*
