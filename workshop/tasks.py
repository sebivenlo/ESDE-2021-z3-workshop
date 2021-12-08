# For testing purposes only
from z3 import *
s = Solver()
print(s.check())
print(s.model())
