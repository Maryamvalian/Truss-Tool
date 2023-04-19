# Makefile
PYTHON = python3
PIP = pip3
PROJECT_DIR = project741
.PHONY: setup run test
setup:
    $(PIP) install -r requirement.txt


run:
    $(PYTHON) $(PROJECT_DIR)/src/control.py Testcases/valid_crane.txt


test:
    $(PYTHON)  pytest 


