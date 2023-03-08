import numpy as np

def getfile(f):
    f.readline()
    n = int(f.readline())
    f.readline()
    J=np.ndarray((n,2))
    for i in range(0,n):
        location=f.readline().split()
        J[i][0] = float(location[0])
        J[i][1] = float(location[1])

    f.readline()
    M=np.ndarray((n,2))
    for i in range(0,n):
        location=f.readline().split()
        M[i][0] = float(location[0])
        M[i][1] = float(location[1])
    f.readline()
    F=np.ndarray((n,2))
    for i in range(0,n):
        location=f.readline().split()
        F[i][0] = float(location[0])
        F[i][1] = float(location[1])
    f.readline()
    p = float(f.readline())
    f.readline()
    r=float(f.readline())

    return n,J,M ,F ,p,r 