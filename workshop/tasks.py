# For testing your Docker Z3 setup
# Proper tasks will be added later
from z3 import *
s = Solver()
print(s.check())
print(s.model())
