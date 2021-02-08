
# ##generetor using way
# def getFunc(num):
#   for i in range(0,num):
#     yield i
#     print("Generator is working!")
# for data in getFunc(5):
#   print(data)

from time import*
from  datetime import*

##
def countdays(date1,date2):
  retDays=0
  year,month,day=date1.split('/')
  sDay=date(int(year),int(month),int(day))
  year,month,day=date2.split('/')
  eDay=date(int(year),int(month),int(day))
  diffDay=eDay-sDay
  retDays=diffDay.days
  return retDays

def getDay(t):
  weeks=['Monday','Tuesday','Wednesday','','Thusday','Saturday','Sunday']
  return weeks[t.tm_wday]

startDate,curData,tm='','',None

if __name__=="__main__":
  startDate=input("Start date>>Year/Month/day-->")
  tm=localtime()
  curData=str(tm.tm_year)+'/'+str(tm.tm_mon)+'/'+str(tm.tm_mday)
  print(countdays(startDate,curData),'day have passed from',startDate,'until',curData)
  print("Then Tudey is ",getDay(tm))