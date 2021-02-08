import shutil
import os


print("Do you want to make a folder??")
num=0; fNname=""
while True:
  num=int(input("Enter <1> make a folder <2> delete a folder <3> program exit>>"))
  if num==1:
    fNname=input("Enter file name that you want to create>>")
    if os.path.exists("A:/"+fNname+"/"):
      print("%s Folder already exist! "% fNname)
    else:
      os.mkdir("A:/"+fNname+"/")
      print("You have created <<A:/%s/>> Folder"% fNname)
  elif num==2:
    fNname=input("Enter fale name that you want to delete>>")
    shutil.rmtree("A:/"+fNname+"/")
    print("<<A:/%s/>> Folder deleted!"%fNname)
  else:
    break


