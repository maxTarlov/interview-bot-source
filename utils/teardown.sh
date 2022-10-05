INTERVIEW_BOT_SOURCE_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/..

if [[ $(which python) == "$INTERVIEW_BOT_SOURCE_DIR/.venv/bin/python" ]]; then 
    deactivate
fi

rm -r $INTERVIEW_BOT_SOURCE_DIR/.venv
