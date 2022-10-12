#!/bin/bash

# Load the Anaconda module
module load Anaconda3
eval "$(conda shell.bash hook)"

# Create a new environment for MIALab
conda create --name mialab python=3.8

# Activate the new environment
conda activate mialab

# Install the MIALab dependencies
pip install -r requirements.txt


# CONFLICTS:
# daal4py 2021.3.0 requires daal==2021.2.3, which is not installed.
# numba 0.54.1 requires numpy<1.21,>=1.17, but you have numpy 1.23.3 which is incompatible.