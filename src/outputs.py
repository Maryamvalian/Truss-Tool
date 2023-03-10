def writefile(msg):
    outputfile = open("output.txt", "w")
    
    print("Truss Results:\n ", end="", file=outputfile)
    print(msg,end="",file=outputfile)
    
    outputfile.close()