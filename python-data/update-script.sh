#!/usr/bin/bash

set -e

# Make sure isc is up to date.
git -C ~/ncas-isc pull

# Update the files.
cp ~/ncas-isc/python-data/exercises/ex04_cf_python.ipynb ~/my-isc-work/python-data/exercises/ex04_cf_python.ipynb
cp -r ~/ncas-isc/python-data/data/* ~/my-isc-work/python-data/data
cp ~/ncas-isc/python-data/solutions/ex04_cf_python.ipynb ~/my-isc-work/python-data/solutions/ex04_cf_python.ipynb
cp -r ~/ncas-isc/python-data/notebooks/* ~/my-isc-work/python-data/notebooks
