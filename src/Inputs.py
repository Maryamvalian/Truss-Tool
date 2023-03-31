import numpy as np
import specif

def verify(n,m,J,M,F,p,r):
    flag=True
    if (n<specif.constants.n_min):
        flag=False
    if (n>specif.constants.n_max):
        flag=False    
    if (m<specif.constants.m_min):
        flag=False    
    if (m>specif.constants.m_max):
        flag=False    
    for i in range (0,n):
        if (F[i][0]<specif.constants.f_min):
            flag=False    
        if (F[i][1]<specif.constants.f_min): 
            flag=False
        if (F[i][0]>specif.constants.f_max):
            flag=False    
        if (F[i][1]>specif.constants.f_max): 
            flag=False     
        if (J[i][0]<specif.constants.d_min):
            flag=False    
        if (J[i][1]<specif.constants.d_min): 
            flag=False
        if (J[i][0]>specif.constants.d_max):
            flag=False    
        if (J[i][1]>specif.constants.d_max): 
            flag=False         
    if (n>m):
        flag=False    
    if (p>n):
        flag=False    
    if (r>n):
        flag=False    
    if ((p==0) and (r==0)):
        flag=False    
    for i in range (0,n):
        if (M[i][0]==M[i][1]):
            flag=False    



    return flag



def getfile(f):
    f.readline()
    n = int(f.readline())
    f.readline()
    J=np.zeros((n+1, 2))
    for i in range(1,n+1):
        location=f.readline().split()
        J[i][0] = float(location[0])
        J[i][1] = float(location[1])

    f.readline()
    m = int(f.readline())
    f.readline()
    M=np.zeros((m+1, 2))
    for i in range(1,m+1):
        location=f.readline().split()
        M[i][0] = int(location[0])
        M[i][1] = int(location[1])
    f.readline()
    F=np.zeros((n+1, 2))
    for i in range(1,n+1):
        location=f.readline().split()
        F[i][0] = float(location[0])
        F[i][1] = float(location[1])
    f.readline()
    p = int(f.readline())
    f.readline()
    r=int(f.readline())

    return n,m,J,M,F,p,r 