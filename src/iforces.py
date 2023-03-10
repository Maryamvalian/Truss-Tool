import numpy as np
import math

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
        if ux<0:
            theta[i]=1.5708-math.atan(uy/ux)     #90 degree=1.5708 rad
        else:
            theta[i]=math.atan(uy/ux)
    return theta
#--------------------------------------------------------------
def insert(a,e,m):
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
                done=True 
      
#--------------------------------------------------------------
def gaussian(n,m,J,M,F,p,r):
    A=np.zeros((m,m))
    b=np.zeros((m,1))
    angles=findTheta(n,m,J,M)
    for i in range(1,n):     
        eq=np.zeros((2,m))
        for j in range (1,m+1):
            if M[j][0]==i or M[j][1]==i:
                eq[0][j-1]=math.cos(angles[j])
                eq[1][j-1]=math.sin(angles[j])
        #omit repititive equations     
        insert(A,eq[0],m)
        insert(A,eq[1],m)
    return A,b
            


