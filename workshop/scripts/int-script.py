from z3 import *
x, y = Int('x'), Int('y')
s = Solver()
s.add(x + y == 42)
s.add(x < 6 * y)
s.add(x % 2 == 1)
print(s.check())
print(s.model())