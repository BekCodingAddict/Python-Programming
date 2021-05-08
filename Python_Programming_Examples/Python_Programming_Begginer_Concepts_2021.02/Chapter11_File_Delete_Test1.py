##File deleting function 
def file_delete(fName):
  import os
  fName="";fName=input("Enter the File name that you want to delete >>")
  if os.path.exists(fName):
    print("%s file deleted!"% fName)
    os.remove(fName)
  else:
      print("%s file is not exist!"% fName)

##Check the file size by bytes
def file_size_check(fName):
  import os.path
  print("%s file size is %d bytes "%(fName,os.path.getsize(fName)))

##This function make a zip file
def compress_Zip(fName):
  import zipfile
  fName=input("Enter the file name that you want to compress zip >>")
  zipName=input("Enter the new zip file name >>")
  newZip=zipfile.ZipFile(zipName+".zip","w")
  newZip.write(fName,compress_type=zipfile.ZIP_DEFLATED)
  newZip.close();
  print("%s file has compressed to zip file!"%fName)

#this function extract zip file
def extract_zip(fName):
  import zipfile
  fName=input("Enter the zip file name that you want to extract >>")
  extZip=zipfile.ZipFile(fName,"r")
  extFolder=input("Enter the folder name that you want to save into >> ")
  extZip.extractall(extFolder)
  print("Zip file extracted into %s folder"% extFolder)
  extZip.close()


fileName=""; extract_zip(fileName)