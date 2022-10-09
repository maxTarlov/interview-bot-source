#!/bin/bash

INTERVIEW_BOT_SOURCE_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "Setting up virtual environment..."
python3 -m venv $INTERVIEW_BOT_SOURCE_DIR/.venv
source $INTERVIEW_BOT_SOURCE_DIR/.venv/bin/activate
pip install -r $INTERVIEW_BOT_SOURCE_DIR/cloud_function/requirements.txt

echo "Copying answers to cloud_function/data..."
cp $INTERVIEW_BOT_SOURCE_DIR/data/answers.json $INTERVIEW_BOT_SOURCE_DIR/cloud_function/data/answers.json

python $INTERVIEW_BOT_SOURCE_DIR/utils/setup_cloud_function.py

echo "Done."