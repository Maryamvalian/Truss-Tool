import numpy as np
from scipy import linalg
import math
import React

def findTheta(n,m,J,M):
    theta=np.zeros(m+1)
    for i in range(1,m+1):
        end1=int(M[i][0])
        end2=int(M[i][1])
        if J[end1][1]>J[end2][1]:
            ux=J[end1][0]-J[end2][0]
            uy=J[end1][1]-J[end2][1]
        else:
            ux=J[end2][0]-J[end1][0]
            uy=J[end2][1]-J[end1][1]
        if ux==0:    
             #avoid divide by zero when ux=0
            theta[i]=1.5708
        else:
            if ux<0:
                theta[i]=1.5708-math.atan(uy/ux)     
                #90 degree=1.5708 rad
            else:
                theta[i]=math.atan(uy/ux)
    return theta
#--------------------------------------------------------------
def insert(a,b,e,m,sum):
    #This module check a row of equations(e) if not repetitive in A, add it to 
    # matrix for equation solver, other wise ignore it.
    dup=False
    done=False
    for i in range (0,m):
        same=0
        for j in range (0,m):
            if a[i][j]==e[j]:
                same+=1
        if same==m:
            dup=True
    if dup==False:
        for i in range (0,m):
            if done==False and np.count_nonzero(a[i])==0:
                a[i]=e
                b[i]=-sum
                done=True 
      
#--------------------------------------------------------------
def internals(n,m,J,M,F,p,r):
    #This module creates eqiulibrium equations for each node. 
    # Coeficients of equations are inserted in Matrix A and vector b.
    A=np.zeros((m,m))
    b=np.zeros((m,1))
    (px,py,ry)=React.find_react(n,J,F,p,r)
    angles=findTheta(n,m,J,M)
    for i in range(1,n):     
        eq=np.zeros((2,m))
        for j in range (1,m+1):
            if M[j][0]==i or M[j][1]==i:
                eq[0][j-1]=math.cos(angles[j])
                #Eqiulibrium equations in X-direction
                eq[1][j-1]=math.sin(angles[j])
                #Eqiulibrium equations in Y-direction
        sum1=0
        sum2=0    
        sum1+=F[i][0]
        sum2+=F[i][1]  
        if p==i :
            sum1+=px
            sum2+=py
        if r==i :
            sum2+=ry
        #prevent repititive equations     
        insert(A,b,eq[0],m,sum1)
        insert(A,b,eq[1],m,sum2)
    I=linalg.solve(A, b) 
    I=np.round(I,2)   
    return I
            


