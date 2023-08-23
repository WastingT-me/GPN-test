#/bin/bash

#create venv
python -m venv ./.venv
./.venv/bin/activate
echo "Python virtual env created successfully"

#installing libraries from requirements.txt
pip install -r requirements.txt
echo "Libraries installing successfully"

python run.py

