#!bin/bash

DIR="${0%/*}"

rm -r $DIR/.venv
$DIR/bot_function/teardown.sh
