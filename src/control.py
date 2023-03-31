import Inputs
import sys
import React
import iforces
import outputs


#input truss via file
filename = sys.argv[1]
f = open(filename, "r")
(n,m,J,M,F,p,r)=Inputs.getfile(f)
f.close()

#input verification
check=Inputs.verify(n,m,J,M ,F ,p,r)
if (check==True):
    raise Exception("Bad Input Parameter")

#mirror input 
print("Given Truss with",n,"Joints\n",J,"\n Members:",M,"\n E forces:\n",F,"\n Pinned Support at",p," , Roller support at",r)

#compute support reactions
(px,py,ry)=React.find_react(n,J,F,p,r)

#compute internal forces
I=iforces.internals(n,m,J,M,F,p,r)

#validation
outputs.valid(px,py,ry,I,n,m,J,M,p,r,F)

#Output 
outputs.writefile(px,py,ry,I)




