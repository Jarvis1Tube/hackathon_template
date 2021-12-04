#!/bin/sh

ALL_PYTHON_FILES=$(git ls-files -om --exclude-standard '*.py')

pylint $ALL_PYTHON_FILES --rcfile=.pylintrc

mypy $ALL_PYTHON_FILES