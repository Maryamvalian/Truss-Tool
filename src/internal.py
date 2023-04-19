import numpy as np
from scipy import linalg
import math



def insert(a,b,e,m,sum):
    #This module check a row of equations(e) if not repetitive in A, add it to A,b
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
    (px,py,ry)=find_react(n,J,F,p,r)
       
    for i in range(1,n):     
        eq=np.zeros((2,m))
        j=1
        while j<m+1:       #for j in range (1,m+1):
            if  (M[j][0]==i)or(M[j][1]==i) :
                if M[j][0]==i:
                    end=int(M[j][1])
                else:
                    end=int(M[j][0])
                uy=J[end][1]-J[i][1]
                ux=J[end][0]-J[i][0]
                if ux==0:    #90 degree=1.5708 rad, Avoid divide by zero
                    theta=1.5708
                    coef_x=0
                    coef_y=uy/abs(uy)
                else:
                     if uy==0:
                         theta=math.atan(abs(uy/ux))
                         coef_x= (ux/abs(ux))
                         coef_y= 0
                     else:
                         theta=math.atan(abs(uy/ux))
                         coef_x= (ux/abs(ux))*math.cos(theta)
                         coef_y= (uy/abs(uy))*math.sin(theta)
                eq[0][j-1]=coef_x
                #Eqiulibrium equations in X-direction
                eq[1][j-1]=coef_y
                #Eqiulibrium equations in Y-direction
            j+=1
		# equations in x-axis direction are like a1I1+a2I2+...+anIn=b we put the coef_x : a1,a2,...an to the eq[0][j-1]	and b to sum1
        sum1=0
		# equations in y-axis direction are like a1I1+a2I2+...+anIn=b we put the coef_x : a1,a2,...an to the eq[1][j-1]	and b to sum2
        sum2=0    
        sum1+=F[i][0]
        sum2+=F[i][1]  
        if p==i :
            sum1+=px
            sum2+=py
        if r==i :
            sum2+=ry
        #Add eq[0],eq[1] to A matrix,and Add sum1,sum2 to Vector b by calling insert     
        insert(A,b,eq[0],m,sum1)
        insert(A,b,eq[1],m,sum2)
        
    I=linalg.solve(A, b) 
    
    I=np.round(I,2) 
    
    
    
    return (px,py,ry,I)

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


