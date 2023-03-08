import  numpy as np
from scipy import linalg

def find_react(n,J,F,p,r):
    A = np.zeros((2,2))
    b = np.zeros((2,1))
    sum=0
    for i in range(1,n+1):
        sum = F[i][0] + sum
    px=-sum 
    #sec equation Y direction
    sum=0
    for i in range(1,n+1):
        sum = F[i][1] + sum 
    A[0][0]=1          #Py
    A[0][1]=1           #Ry
    b[0][0]=-sum
    #create eq Sum(M)=0 pivot :(0,0)
    sum=0
    for i in range(1,n+1):
        sum = (F[i][1])*J[i][0] + sum       #Perpendicular F, distance to (0,0)
    A[1][0]=J[p][0]          #Py
    A[1][1]=J[r][0]           #Ry
    b[1][0]=-sum
    #Solve equations
    x = linalg.solve(A, b)
    py=float(x[0])
    ry=float(x[1])
    return px,py,ry