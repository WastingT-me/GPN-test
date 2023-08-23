#/bin/bash

#create venv
python3 -m venv ./.venv
source .venv/bin/activate
echo "Python virtual env created successfully"

#installing libraries from requirements.txt
pip install -r requirements.txt
echo "Libraries installing successfully"

python run.py

