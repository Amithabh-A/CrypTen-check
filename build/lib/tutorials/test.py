import os
import sys

# Get the directory containing the Par directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the Par directory to the sys.path
sys.path.append(parent_dir)


from examples.mpc_linear_svm.mpc_linear_svm import *
