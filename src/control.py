#import inputTRUSS
import Inputs
import sys

#input via keyboard
#(n,J,M,F,p,r)=inputTRUSS.gettruss()
#input via file
filename = sys.argv[1]
f = open(filename, "r")
# read input
(n,J,M,F,p,r)=Inputs.getfile(f)
f.close()
#inParams = (n,J,M,F,p,r)
#calledfunc = "control"

print("Given Truss with",n,"Joints\n",J,"\n Members:",M,"\n E forces:\n",F,"\n Pinned Support at",p," , Roller support at",r)
