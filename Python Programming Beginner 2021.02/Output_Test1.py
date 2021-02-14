import sqlite3

def InputDates():
  con,cur=None,None;id,uname,email="","","";birth=""; sql=""
  con=sqlite3.connect("C://Users//titan//OneDrive//Desktop//Python Programming//Python_Beginner//NaverDB")
  cur=con.cursor()
  choose=0
  while True:
    print("<1> Enter User Dates  <2> Exit")
    choose=int(input("Enter number for Menu >>"))
    if choose==1:
      id=input("Enter User ID >>")
      uname=input("Enter User Name >>")
      email=input("Enter User Email >>")
      birth=input("Email User Birth Dates >>")

      sql="INSERT INTO UserName VALUES('"+id+"','"+uname+"','"+email+"','"+birth+"')"
      cur.execute(sql)
    elif choose==2:
      print("Data Base Programm has Closed!!")
      break
  con.commit()
  con.close()

def PrintDates():
  con,cur=None,None;id,uname,email,birth="","","",""
  row=None

  con=sqlite3.connect("C://Users//titan//OneDrive//Desktop//Python Programming//Python_Beginner//NaverDB")
  cur=con.cursor()

  cur.execute("SELECT * FROM UserName")
  print("  User Id    User Name   User Emal Address      User Birth Dates \n")
  print("********************************************************************")
  while True:
    row=cur.fetchone()
    if row==None:
      break
    id=row[0]
    uname=row[1]
    email=row[2]
    birth=row[3]
    print("  %5s    %10s    %20s   %s "%(id,uname,email,birth))
  print("********************************************************************")
  con.close()


def DeleteDates():
  con,cur=None,None;id,uname,email,birth="","","",""
  delData=""
  con=sqlite3.connect("C://Users//titan//OneDrive//Desktop//Python Programming//Python_Beginner//NaverDB")##--> DATA BASE SOURSE CODE ADDRESS FOLDER
  cur=con.cursor()
  delData=str(input("Enter the User Id that you want to delete >>"))
  # try:
  cur.execute("DELETE FROM UserName WHERE id='%s'"% delData)
  # except:
  # print("It has occoured error!")
  con.commit()
  con.close()

def UpdateDates():
  cur,con=None,None;id,uname,email,birht="","","",""
  upId,upDate="","";upDate2=""; choose=0
  con=sqlite3.connect("C://Users//titan//OneDrive//Desktop//Python Programming//Python_Beginner//NaverDB")
  cur=con.cursor()
  print("Select tha dates for you want to change ")
  print("<1> Id <2> User Name <3> User Email <4> User Birth")
  choose=int(input(">>"))
  if choose==1:
    try:
      upDate=str(input("Enter Id Name that you want to change >>"))
      upDate2=str(input("Enter New Id name >>"))
      cur.execute("UPDATE UserName SET id='%s' WHERE id='%s' "%(upDate2,upDate))
      print("Data has changed successfully!")
    except:
      print("Error: There was something went wrong!")
  elif choose==2:
    try:
      upDate=str(input("Enter Id Name that you want to change >>"))
      upDate2=str(input("Enter New User Name >>"))
      cur.execute("UPDATE UserName SET userName='%s' WHERE id='%s' "%(upDate2,upDate))
      print("Data has changed successfully!")
    except:
      print("Error: There was something went wrong!")

  elif choose==3:
    try:
      upDate=str(input("Enter Id Name that you want to change >>"))
      upDate2=str(input("Enter New Email Address name >>"))
      cur.execute("UPDATE UserName SET email='%s' WHERE id='%s' "%(upDate2,upDate))
      print("Data has changed successfully!")
    except:
      print("Error: There was something went wrong!")
  elif choose==4:
    try:
      upDate=str(input("Enter Id Name that you want to change >>"))
      upDate2=str(input("Enter New Birth Date >>"))
      cur.execute("UPDATE UserName SET birthday='%s' WHERE id='%s' "%(upDate2,upDate))
      print("Data has changed successfully!")
    except:
      print("Error: There was something went wrong!")


  con.commit()
  con.close()


if __name__ == '__main__':
  print('''
  <1> Input Dates 
  <2> Print Dates
  <3> Delete Dates
  <4> Upgrade User Dates
  <None> Exit
  ''')
  choose=int(input("Enter the Menu number >>"))
  if choose==1:
    InputDates()
  elif choose==2:
    PrintDates()
  elif choose==3:
      DeleteDates()
  elif choose==4:
    UpdateDates()
  else:
    print("Program has closed!")

    
