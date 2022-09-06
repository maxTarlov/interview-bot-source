#!bin/bash

# create virtual environment for project
python3 -m venv ".venv"
source .venv/bin/activate

pip install -r requirements.txt

chmod u=rwx bot_function/setup.sh
./bot_function/setup.sh
