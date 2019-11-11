# b-dev-test

Python Wrapper for B dev

## How to use

### Init your PC :

from root folder on the repo :

* create a venv
```
python3.7 -m venv python3.7-venv
```

* install colored plugin
```
./python3.7-venv/bin/activate
pip install colored
```

### Setup a new exercice
for each exercice, create a folder - exemple : my_exo_1 - and a python script inside witj the same name.
Exemple : ./my_exo1/my_exo1.py

Inside the exercice foldre create a "sample" folder and put in it the input/output files.


### Launch your code 

Write your code in the exercice file, exemple in ./my_exo1/my_exo1.py

**In your code, you need to put all output line in the **

In Wrapper.py, change the settings with the exercice you working on :

################################ SETTINGS
ex_to_launch = "M2016-ex1"
input_to_open = "input1.txt"
output_to_compare = "output1.txt"
################################

Simply launch wrapper.py

If you using VSCODE, launch.json is set to always launching ./wrapper.py, so you can F5 directly from exercice tab to launch it with wrapper.
