import numpy as np

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

    return n,m,J,M ,F ,p,r 