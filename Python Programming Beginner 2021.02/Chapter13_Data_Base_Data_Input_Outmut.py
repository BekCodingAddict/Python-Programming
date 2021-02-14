import sqlite3
##declarate variable

con,cur=None,None; id,uName,email="","",""; birth=0
con=sqlite3.connect('C://Users//titan//OneDrive//Desktop//Python Programming//Python_Beginner//NaverDB')
cur=con.cursor()
row=None

cur.execute("SELECT * FROM UserName")
print("User ID      User Name       User Email       User Birth Data   ")
print("________________________________________________________________")
i=int(0)
while (True):
  row=cur.fetchone()
  if row==None:
    break;
  id=row[0]
  uName=row[1]
  email=row[2]
  birth=row[3]
  print("%5s  %15s  %20s   %d "%(id,uName,email,birth))

con.close()
