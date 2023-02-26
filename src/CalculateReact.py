#      Calculate Support Reactions
from sympy import *
#test case (temporary)
n=3
J=[[0, 0],[1, 1],[2, 0],[3,1],[4,0],[5,1]]
M=[[1, 2],[1, 3],[2 ,3],[2,4],[3,4],[3,5],[4,5],[4,6],[5,6]]
F=[[0 ,0],[0, -5],[0 ,0],[-3,-2],[0,0],[0,0]]
p=0   # location(0,0)
r=2   #location(2,0)
#Support Reaction 
# Assumption: Only One pinned support p , One roller support r
# create first Equation- Sum(Fx)=0
sum=0
for i in range(len(F)):
    sum = F[i][0] + sum
PX=-sum 
print("\n Reactions Calculated Successfully. \n PX:",PX)

#create Equation  : SUM(FY)=0
#PY Pinned support Y-reaction, RY poller support Y-reaction   
sum=0
for i in range(len(F)):
    sum = F[i][1] + sum 
PY,RY= symbols('PY RY')
e1=Eq(PY+RY,-sum)
#create eq Sum(M)=0 pivot :(0,0)
sum=0
for i in range(len(F)):
    sum = (F[i][1])*J[i][0] + sum       #Perpendicular F, distance to (0,0)
e2=Eq(PY*J[p][0]+RY*J[r][0],-sum)      
#Solve All equations
sol=solve((e1,e2),(PY,RY))
print(sol)