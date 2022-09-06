#!/bin/bash
DIR="${0%/*}"

source $DIR/../.venv/bin/activate

mkdir $DIR/source/
mkdir $DIR/source/resources
wget --output-document $DIR/source/resources/answers.json\
  https://raw.githubusercontent.com/maxTarlov/interview-bot-data/main/answers.json

# python utils/set_up_deployable.py