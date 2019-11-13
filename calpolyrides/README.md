# Back End Documentation


## Setup

Prereq:
Python
Pip

Install virtualenv
https://virtualenv.pypa.io/en/latest/

Install virtualenvwrapper
https://virtualenvwrapper.readthedocs.io/en/latest/

### Create Post activate script

Replace my paths with you're paths
vim /Users/garrettlew/.virtualenvs/postactivate
```
#!/bin/bash
# This hook is sourced after every virtualenv is activated.

export DJANGO_SETTINGS_MODULE='calpolyrides.settings'
export PYTHONPATH='/Users/garrettlew/Documents/calpoly/CSC308-Rideshare/calpolyrides'
cd ~/Documents/calpoly/CSC308-Rideshare
```
deactivate env and reactivate to check if the script worked
See if DJANGO_SETTINGS_MODULE and PYTHONPATH environment variable has been set correctly

Install Django in the virtual environment
```
pip install django
```

Install django rest framework
```
pip install djangorestframework
```




