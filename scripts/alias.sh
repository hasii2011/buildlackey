#
# meant to be sourced in
#
packageMe() {
clear
cd scripts || exit
./packageme.sh '$*'
}

alias cleanup='clear;   cd scripts;  ./cleanup.sh;   cd -'
alias runmypy='clear;   cd scripts;  ./runmypy.sh;   cd -'
alias runtests='clear;  cd scripts;  ./runtests.sh;  cd -'

alias package='clear; packageMe deploy'
