#!/bin/bash

# Run this function whenever you change something in the data directory to make sure that you test 
# and deploy the most up-to-date data with your cloud function.

INTERVIEW_BOT_SOURCE_LINK=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/..
# Linux requires readlink -f, OSX requires that there be no options smh
INTERVIEW_BOT_SOURCE_DIR=$( readlink -f $INTERVIEW_BOT_SOURCE_LINK || readlink $INTERVIEW_BOT_SOURCE_LINK )

echo "Copying answers to cloud-function/data..."

cp $INTERVIEW_BOT_SOURCE_DIR/data/answers.json $INTERVIEW_BOT_SOURCE_DIR/cloud-function/data/answers.json
cp $INTERVIEW_BOT_SOURCE_DIR/data/config.json $INTERVIEW_BOT_SOURCE_DIR/cloud-function/data/config.json

python $INTERVIEW_BOT_SOURCE_DIR/utils/setup_cloud-function.py
