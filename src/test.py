from sympy import *
X,Y,Z,T= symbols('X Y Z T')
e1=Eq(Z+2*X-6*Y,20)   
e2=Eq(5*X+2*Y-6*T,0)
e3=Eq(X-Y+2*Z-T,4)
e4=Eq(11*X+5*Z-Y-3*T,3)
sol=solve((e1,e2,e3,e4),(X,Y,Z,T))
print(sol)
