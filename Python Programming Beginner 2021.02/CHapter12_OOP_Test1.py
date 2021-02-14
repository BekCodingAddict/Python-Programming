class Car:
  color=""
  speed=0
  def getColor(self,color):
    self.color=color
  def upSpeed(self,value):
    self.speed+=value
  def downSpeed(self,value):
    self.speed+=value
  def display(self):
    print("The Car's current speed is %d "%self.speed)
    print("The Car's current color is %s"% self.color)

myCar1=Car()
myCar1.getColor("Blue")
myCar1.upSpeed(40)
myCar1.display() 
