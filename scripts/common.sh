#
# Meant to be sourced
#

function changeToProjectRoot {

    areHere=$(basename "${PWD}")
    export areHere
    if [[ ${areHere} = "scripts" ]]; then
        cd ..
    fi

    if [[ ${areHere} = "src" ]]; then
        cd ..
    fi
}

function checkStatus {

    status=$1
    testName=$2

    echo "checkStatus ${testName} -- ${status}"
    if [ "${status}" -ne 0 ]
    then
        exit "${status}"
    fi
}

