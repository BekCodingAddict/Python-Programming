import os
inFile,outFile=None,None
inStr="";fName="";inList=[];fName2=""
outList=[]
fName=input("Entert the file name that you want to copy from (if exist files mark '/' or '\\') >>")
fName2=input("Enter the file name that you want to copy into if exist files mark as '/' or '\\' >>")

if os.path.exists(fName):
  inFile=open(fName,"r")
  inList=inFile.readlines()
  i=0
  print("This words will be Copy to %s"%fName2)
  for inStr in inList:
    i+=1
    print("%d) %s"%(i,inStr),end="")
  outFile=open(fName2,"w")
  for inStr in inList:
    outFile.writelines(inStr)
  inFile.close()
  outFile.close()
  outStr=""
  print("%s file copyed into %s file"% (fName,fName2))
  outFile=open(fName2,"r")
  outList=outFile.readlines()
  for outStr in outList:
    i+=1
    print("%d) %s"%(i,outStr),end="")
  outFile.close()
else:
  print("%s file is not exist!"%fName)



  
