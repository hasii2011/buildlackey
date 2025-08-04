#
# meant to be sourced in
#
packageMe() {
clear
cd scripts || exit
./packageme.sh '$*'
# shellcheck disable=SC2164
cd ..
}


alias cleanup='clear;   cd scripts;  ./cleanup.sh;   cd -'
alias runmypy='clear;   cd scripts;  ./runmypy.sh;   cd -'

alias package='clear; packageMe deploy'
