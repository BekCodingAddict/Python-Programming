class Car:
  color=""
  speed=0
  def __init__(self,value1,value2):
    self.color=value1
    self.speed=value2

  def getColor(self,color):
    self.color=color
  def upSpeed(self,value):
    self.speed+=value
  def downSpeed(self,value):
    self.speed+=value
  def display(self):
    print("The Car's current speed is %d "%self.speed)
    print("The Car's current color is %s"% self.color)

myCar1=Car("Green",200)
myCar1.display()