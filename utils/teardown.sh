#!/bin/bash

# Script to undo everything that setup.sh does. This is useful for testing setup.sh

INTERVIEW_BOT_SOURCE_LINK=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/..
# Linux requires readlink -f, OSX requires that there be no options smh
INTERVIEW_BOT_SOURCE_DIR=$( readlink -f $INTERVIEW_BOT_SOURCE_LINK || readlink $INTERVIEW_BOT_SOURCE_LINK )

if [[ $(which python) == "$INTERVIEW_BOT_SOURCE_DIR/.venv/bin/python" ]]; then 
    deactivate
fi

rm -r $INTERVIEW_BOT_SOURCE_DIR/.venv

rm -r $INTERVIEW_BOT_SOURCE_DIR/cloud-function/data
