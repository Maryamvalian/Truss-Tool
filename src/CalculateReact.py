#      Calculate Support Reactions
from sympy import *


x,y,z= symbols('x y z')
e1=Eq(2*x-y-z,0)
e2=Eq(-4*x+2*y-5*z,6)
e3=Eq(x+y-20*z,5)
sol=solve((e1,e2,e3),(x,y,z))
print(sol)