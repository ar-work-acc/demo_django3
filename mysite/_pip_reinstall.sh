#!/bin/bash
pip freeze | xargs pip uninstall -y
pip install -r requirements.txt

# pass an argument greater than 0 to install local dependencies, too
if [ "$1" -gt 0 ]; then
  pip install -r requirements.local.txt
fi
