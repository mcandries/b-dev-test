# b-dev-test

Python Wrapper for B dev

## Init your PC :

You can do it manually or via VSCODE Task :

**Manually :**

From root folder on the repo :

* create a venv
```
python3.7 -m venv python3.7-venv
```

* install colored plugin
```
./python3.7-venv/bin/activate
pip install colored
```

**From VSCODE Task :**

Ctrl+alt+T ==> "Init VENV"
Then select the new venv as venv for the project, and install linter.

after done :
Ctrl+alt+T ==> "Install modules"


## Setup a new exercice
for each exercice, create a folder and a python script inside with the same name.
Exemple : ./my_exo1/my_exo1.py

Inside the exercice folder create a "sample" folder and put in it the input/output files from battle dev.


## Launch your code 

Write your code in the exercice file, exemple in ./my_exo1/my_exo1.py, as it is in the web interface of battle Dev.

In Wrapper.py, change the settings with the exercice you working on :

```python
################################ SETTINGS
ex_to_launch = "M2016-ex1"
input_to_open = "input1.txt"
output_to_compare = "output1.txt"
################################
```

Then simply launch wrapper.py

**If using VSCODE**, launch.json is set to always launching ./wrapper.py with the current openned script, so you can F5 directly from exercice tab to launch it with wrapper :)
