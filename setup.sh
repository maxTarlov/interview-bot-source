#!/bin/bash

# This script is for setting up the development environment getting the cloud function ready for deployment

INTERVIEW_BOT_SOURCE_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "Setting up virtual environment..."
python3 -m venv $INTERVIEW_BOT_SOURCE_DIR/.venv
source $INTERVIEW_BOT_SOURCE_DIR/.venv/bin/activate
pip install -r $INTERVIEW_BOT_SOURCE_DIR/requirements.txt
pip install -r $INTERVIEW_BOT_SOURCE_DIR/cloud-function/requirements.txt

if [ ! -d "$INTERVIEW_BOT_SOURCE_DIR/cloud-function/data" ]; then 
    mkdir $INTERVIEW_BOT_SOURCE_DIR/cloud-function/data
fi

$INTERVIEW_BOT_SOURCE_DIR/utils/refresh_cloud_function_data.sh

echo "Done."
