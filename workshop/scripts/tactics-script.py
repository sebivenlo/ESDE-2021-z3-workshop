from z3 import *
x, y = Reals('x y')
g = Goal()
g.add(2 < x, Exists(y, And(y > 0, x == y + 2)))
print(g)

t1 = Tactic('qe-light')
t2 = Tactic('simplify')
t = Then(t1, t2)
print(t(g))

