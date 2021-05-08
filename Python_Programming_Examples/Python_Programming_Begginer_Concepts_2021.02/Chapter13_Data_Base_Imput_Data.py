import sqlite3

## Declaret variable
con,cur=None,None;sql,id,uName,email,birth=[""]*5;num=0
##main code
con=sqlite3.connect("C://Users//titan//OneDrive//Desktop//Python Programming//Python_Beginner//NaverDB")
cur=con.cursor()

while (True):
  print('''
  <1> Enter ID
  <2> Enter User Name
  <3> Enter Email Address
  <4> Enter Birth Dates 
  <5> Exit
  ''')
  num=int(input("Enter the number for Menu >>"))
  if num==1:
    id=input("Enter the User Id>>")
  elif num==2:
    uName=input("Enter the UserName >>")
  elif num==3:
    email=input("Enter the User email >>")
  elif num==4:
    birth=input("Enter the User birth data >>")
  else:
    print("Python Data Base Program has closed!")
    break
  sql="INSERT INTO UserName VALUES ('"+id+"','"+uName+"','"+email+"','"+birth+"')"
  cur.execute(sql)

con.commit()
con.close()


