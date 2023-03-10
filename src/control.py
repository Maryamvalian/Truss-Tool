import Inputs
import sys
import React
import iforces
import outputs

#input via file
filename = sys.argv[1]
f = open(filename, "r")
(n,m,J,M,F,p,r)=Inputs.getfile(f)
f.close()
#mirror input 
#print("Given Truss with",n,"Joints\n",J,"\n Members:",M,"\n E forces:\n",F,"\n Pinned Support at",p," , Roller support at",r)
#compute react
(px,py,ry)=React.find_react(n,J,F,p,r)
reactions="Pinned Support X-direction reaction="+str(px)+"\n Pinned Support Y-directed reaction ="+str(py)+"\n Roller Support Y-directed reaction ="+str(ry)
outputs.writefile(reactions)

#
A,b=iforces.gaussian(n,m,J,M,F,p,r)
print(A,b)
