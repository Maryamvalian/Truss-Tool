#     Input Truss Module
#     input : N (number of joints), Joints (location of joints)
#       Members: index of connected joints, Forces( index anf amount of force) 
#       Support(P,R): index of supports (zero if not exists)
 
# **************************************************************
def gettruss():
    n=int (input("Enter the number of Joints:"))
    Joints=[]
# Joint index starts from index 1
    Joints.append(0) 
#input (x,Y) locations for each joint   
    for i in range(0,n):
        Joints.append([float(j) for j in input().split()]) 
    print("Enter Members:")
    Members=[]
    Members.append(0)
    for i in range(0,n):
        Members.append([int(j) for j in input().split()]) 
    print("Enter External Forces:")   
    Forces=[]
    Forces.append(0)
    for i in range(0,n):
        Forces.append([int(j) for j in input().split()]) 
    
    Sp=int (input("Enter the index of Pinned Support:")) 
    Sr=int (input("Enter the index of Roller Support:")) 


    return n,Joints,Members,Forces,Sp,Sr


  

