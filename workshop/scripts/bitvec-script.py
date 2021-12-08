from z3 import *
x = BitVec('x', 8)
s = Solver()
s.add(x + 5 < x - 10)
print(s.check())
print(s.model())
for i in range(8):
 print(s.model().eval(Extract(i, i, x)))

