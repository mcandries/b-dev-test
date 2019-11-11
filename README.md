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
for each exercice, create a folder and a python script inside with the same name.
Exemple : ./my_exo1/my_exo1.py

Inside the exercice folder create a "sample" folder and put in it the input/output files from battle dev.


### Launch your code 

Write your code in the exercice file, exemple in ./my_exo1/my_exo1.py, as it is in the web interface of battle Dev.

In Wrapper.py, change the settings with the exercice you working on :

################################ SETTINGS
ex_to_launch = "M2016-ex1"
input_to_open = "input1.txt"
output_to_compare = "output1.txt"
################################

Simply launch wrapper.py

If using VSCODE, launch.json is set to always launching ./wrapper.py with the current openned script, so you can F5 directly from exercice tab to launch it with wrapper :)
