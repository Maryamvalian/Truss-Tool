
import math
import numpy as np

def valid(px,py,ry,I,n,m,J,M,p,r,F):
    angles=findTheta(n,m,J,M)
    sumx=0
    sumy=0
    #Check Validation in the final jonit n
    for i in range (1,m+1):
        if M[i][0]==n or M[i][1]==n:
            sumx+=I[n-1]*math.cos(angles[n])
            sumy+=I[n-1]*math.sin(angles[n])
    if (p==n):
        sumx+=px
        sumy+=py
    if (n==r):
        sumy+=ry
    sumx+=F[n][0]  
    sumy+=F[n][1]    

    if (not(sumx==0) and (sumy==0)):
        raise Exception("Invalid output")
    writefile(px,py,ry,I)
  

def writefile(px,py,ry,I):
    results="Pinned Support X-direction reaction="+str(px)+"\n Pinned Support Y-directed reaction ="+str(py)+"\n Roller Support Y-directed reaction ="+str(ry)+"\n Internal Forces: \n"+str(I)
    #write results in output file
    outputfile = open("output.txt", "w")
    print("Truss Results:\n ", end="", file=outputfile)
    print(results,end="",file=outputfile)
    outputfile.close()

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