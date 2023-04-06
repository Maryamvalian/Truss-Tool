import iforces
import math

def valid(px,py,ry,I,n,m,J,M,p,r,F):
    angles=iforces.findTheta(n,m,J,M)
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