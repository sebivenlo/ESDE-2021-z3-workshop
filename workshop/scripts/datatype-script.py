from z3 import *
C = Datatype('Colour')
for c in ["red", "green", "blue"]:
    C.declare(c)
CSort = C.create()
s = Solver()
x = Const("x", CSort)
s.add(x != CSort.green)
s.add(x != CSort.red)
if s.check() != sat: exit(1)
print(s.model())

