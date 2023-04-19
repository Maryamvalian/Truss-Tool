import numpy as np
import specif

def verify(n,m,J,M,F,p,r):
    
    if (n<specif.constants.N_MIN):
        print("Invalid Joints")
        return False
    if (n>specif.constants.N_MAX):
        print("Invalid Joints")
        return False    
    if (m<specif.constants.M_MIN):
        print("Invalid Members")
        return False    
    if (m>specif.constants.M_MAX):
        print("Invalid Members")
        return False    
    for i in range (0,n):
        if (F[i][0]<specif.constants.F_MIN):
            print("Invalid force")
            return False    
        if (F[i][1]<specif.constants.F_MIN): 
            print("Invalid force")
            return False
        if (F[i][0]>specif.constants.F_MAX):
            print("Invalid force")
            return False    
        if (F[i][1]>specif.constants.F_MAX): 
            print("Invalid force")
            return False     
        if (J[i][0]<specif.constants.D_MIN):
            print("Invalid location")
            return False    
        if (J[i][1]<specif.constants.D_MIN):
            print("Invalid location") 
            return False
        if (J[i][0]>specif.constants.D_MAX):
            print("Invalid location")
            return False    
        if (J[i][1]>specif.constants.D_MAX):
            print("Invalid location") 
            return False         
    if (n>m):
        print("Invalid Members")
        return False    
    if (p>n):
        print("Invalid Index")
        return False    
    if (r>n):
        print("Invalid lndex")
        return False    
    if ((p==0) and (r==0)):
        print("No support defined")
        return False    
    for i in range (0,n):
        if (M[i][0]==M[i][1]):
            return False    



    return True



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
     #mirror
    print("Given Truss with",n,"Joints\n",J,"\n Members:",M,"\n E forces:\n",F,"\n Pinned Support at",p," , Roller support at",r)
     #verify input
    check=verify(n,m,J,M ,F ,p,r)
    if (check):
        raise Exception("Bad Input Parameter")

    return n,m,J,M,F,p,r 