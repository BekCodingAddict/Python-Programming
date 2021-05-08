def delete_File(fNmae):
  import os
  fName=input("Enter the file name that you want to delete >>")
  try:
    os.remove(fNmae)
    print("File has deleted!")
  except:
    print("%s file is not exist!"% fName)

def string_derectory(myString):
  myString=input("Enter any words >>")
  strPostlist=[];index=0
  while True:
    try:
      index=myString.index("python",index)
      strPostlist.append(index)
      index=index+1
    except:
      break
  print("Pyhton words index >>", strPostlist)

def error_check(num1,num2):
  try:
    num1=input("Enter the frist number >>"); num2=input("Enter the Second number >>")
  except:
    print("It has occoured the error!")
  else:
    print("result >>",num1+"+"+num2+"="+num1+num2)
  finally:
    print("This place allways print!!")

fileName=""; string_derectory(fileName)
error_check(10,20)

