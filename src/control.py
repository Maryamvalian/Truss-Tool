import Inputs
import sys
import React

#input via file
filename = sys.argv[1]
f = open(filename, "r")
(n,m,J,M,F,p,r)=Inputs.getfile(f)
f.close()
#mirror input 
print("Given Truss with",n,"Joints\n",J,"\n Members:",M,"\n E forces:\n",F,"\n Pinned Support at",p," , Roller support at",r)
#compute react
(px,py,ry)=React.find_react(n,J,F,p,r)
#
print("Px,Py,Ry",px,py,ry)
