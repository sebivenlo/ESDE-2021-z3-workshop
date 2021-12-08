# For testing your Docker Z3 setup
# Proper tasks will be added later
# 
# When you see the following output after running the script, everything has been configured correctly:
# sat
# []
#
print("---------------------------------------------------------------------------------")
print("When you see the following output after running the script, everything has been configured correctly:\nsat\n[]")
print("---------------------------------------------------------------------------------")
from z3 import *
s = Solver()
print(s.check())
print(s.model())
