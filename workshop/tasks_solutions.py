# -*- coding: utf-8 -*-
from z3 import *
# Note: 
# When unsolved, the output is shown as:
# sat
# []

# ================================ #
# Task 1: Propositional Logic
# ================================ #
Shoe, Hat = Bools('Shoe Hat')
s = Solver()
# Task 1.1
# TODO: Create a solver object with the following constraints: 
# Shoe V Hat
# = Shoe or Hat
# 
# An example for the syntax: s.add(Or(Not(Shoe, Hat)))
#  not(shoe) or hat = s.add(Or(Not(Shoe), Hat))
### SOLUTION
s.add(Or(Shoe,Hat))
### END SOLUTION
print("\n=== Checking task 1.1 ===\n")
print(s.check())
print(s.model())

Shirt = Bool("Shirt")
s = Solver()
# Task 1.2
# TODO: Create a solver object with the following constraints: 
# ((Shoe ∧ Hat) ∧ Shirt)
# = Shoe and Hat
# 
# An example for the syntax: s.add(Or(Not(Shoe, Hat)))
#  not(shoe) or hat = s.add(Or(Not(Shoe), Hat))
### SOLUTION
s.add(And(And(Shoe,Hat),Shirt))
### END SOLUTION
print("\n=== Checking task 1.2 ===\n")
print(s.check())
print(s.model())

# ================================ #
# Task 2: Solving equations
# ================================ #
# Task 2.1
a, b = Int("a"), Int("b")
s = Solver()
## TODO Add the following equations to the solver:
# a + b = 22
# a < 3 * b
# a % 2 == 1
# The syntax is as follows: s.add(x + y == 1)
### SOLUTION
s.add(a + b == 22)
s.add(a < 3 * b)
s.add(a % 2 == 1)
### END SOLUTION
print("\n=== Checking task 2.1 ===\n")
print(s.check())
print(s.model())

# Task 2.2
x, y = Int("x"), Int("y")
s = Solver()
## TODO Add the following equations to the solver:
# x - y = 0
# x < 19 * y
# a % 2 == 1
# The syntax is as follows: s.add(x + y == 1)
### SOLUTION
s.add(x - y == 0)
s.add(x < 19 * y)
s.add(x % 2 == 1)
### END SOLUTION
print("\n=== Checking task 2.2 ===\n")
print(s.check())
print(s.model())

# ================================ #
# Task 3: Create a custom datatype
# ================================ #
Season = Datatype("Season")
for s in ["spring", "summer", "autumn", "winter"]:
    Season.declare(s)
Season = Season.create()

# Task 3.1
s = Solver()
x = Const("x", Season)
# TODO Add the constraints so that ONLY SPRING is shown
# Syntax: s.add(x != DataType.field)
### SOLUTION
s.add(x != Season.summer)
s.add(x != Season.autumn)
s.add(x != Season.winter)
### END SOLUTION
print("\n=== Checking task 3.1 ===\n")
print(s.check())
print(s.model())

# Task 3.2
s = Solver()
x = Const("x", Season)
# TODO Add the constraints so that SPRING is NOT shown
# Syntax: s.add(x != DataType.field)
### SOLUTION
s.add(x != Season.spring)
### END SOLUTION
print("\n=== Checking task 3.2 ===\n")
print(s.check())
print(s.model())