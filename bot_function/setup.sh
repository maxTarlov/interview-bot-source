#!bin/bash
source ../.venv/bin/activate

mkdir source
mkdir source/resources
wget --output-document source/resources/answers.json\
  https://raw.githubusercontent.com/maxTarlov/interview-bot-data/main/answers.json

# python utils/set_up_deployable.py