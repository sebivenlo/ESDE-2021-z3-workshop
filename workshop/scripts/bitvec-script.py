from z3 import *
x = BitVec('x', 8)
s = Solver()
s.add(x % 2 == 1)
print(s.check())
print(s.model())
for i in range(8):
 print(s.model().eval(Extract(i, i, x)))

