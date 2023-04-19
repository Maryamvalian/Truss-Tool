import Inputs
import sys
import internal
import outputs

#input truss via file
filename = sys.argv[1]
f = open(filename, "r")
(n,m,J,M,F,p,r)=Inputs.getfile(f)
f.close()

#Calculations
(px,py,ry,I)=internal.internals(n,m,J,M,F,p,r)
#print(I)

#validation& output
outputs.valid(px,py,ry,I,n,m,J,M,p,r,F)
