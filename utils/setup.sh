#!bin/bash

# create virtual environment for project
python3 -m venv ".venv"
source .venv/bin/activate

pip install -r requirements.txt

mkdir deployable/resources
wget --output-document deployable/resources/answers.json\
  https://raw.githubusercontent.com/maxTarlov/interview-bot-data/main/answers.json

# python utils/set_up_deployable.py
