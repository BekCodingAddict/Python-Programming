import os.path

# print(os.path.exists("A:/txt/")) ##Check this folder or file exist or not if exist return true not return false
# print(os.path.isfile("A:/txt/Temp2.txt")) ##Check it's file or not if file return True not Return false
# print(os.path.isdir("A:/txt/Temp.txt")) ##Check it's Folder or not if Folder return true not return false

fName="";choose=0
choose=int(input("Enter number <1> File or Folder exist or not <2> Check It's File or Not <3> Check It's Folder or not >>"))
if choose==1:
  fName=input("Enter the File name that you want to check it's exist or not (if File file name.txt if folder folder name/)>>")
  if os.path.exists(fName):
    print("%s File or folder  is exist!"% fName)
  else:
    print("%s File or Folder is not exist!"% fName)
elif choose==2:
  fName=input("Enter the File name that you want to check it's file or not (if File file name.txt if folder folder name/)>>")
  if os.path.isfile(fName):
    print("%s is File!"%fName)
  else:
    print("%s is not File!"%fName)
else:
  fName=input("Enter the File name that you want to check it's Folder or not(if File file name.txt if folder folder name/)>>")
  if os.path.isdir(fName):
    print("%s is Folder!"% fName)
  else:
    print("%s is not Folder "% fName)

