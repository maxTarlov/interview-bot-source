#!bin/bash

DIR="${0%/*}"

# create virtual environment for project
python3 -m venv "$DIR/.venv"
source $DIR/.venv/bin/activate

pip install -r $DIR/requirements.txt

$DIR/bot_function/setup.sh
