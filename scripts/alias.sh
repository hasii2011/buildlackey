#
# meant to be sourced in by .envrc
#
alias cleanup='clear;   cd scripts;  ./cleanup.sh;   cd -'
alias runtests='clear;  cd scripts;  ./runtests.sh;  cd -'
alias runmypy='clear;   cd scripts;  ./runmypy.sh;   cd -'

alias packageme='clear; ./scripts/packageme.sh $*'

alias rmypy='clear; cdir; run_project_mypy.sh; cd -'
alias deploy='clear; packageme deploy'
