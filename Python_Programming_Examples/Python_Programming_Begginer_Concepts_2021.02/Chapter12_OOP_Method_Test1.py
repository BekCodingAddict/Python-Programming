class Line:
  length=0
  def __init__(self,lenght):
      self.length=lenght
      print(self.length,"길이 선이 생선되었다!")

  def __del__(self):
    print(self.length,"길이의 선이 삭제되었다!")

  def __repr__(self):
    return "선의 길이: "+str(self.length)

  def __add__(self,other):
    return self.length+other.lenght

  def __it__(self,other):
    return self.length<other.lenght

  def __eq__(self,other):
    return self.length==other.lenght



myLine=Line(100)
print(myLine)

myLine2=Line(200)
print(myLine2)

