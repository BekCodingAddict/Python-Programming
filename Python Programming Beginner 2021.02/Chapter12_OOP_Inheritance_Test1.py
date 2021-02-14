class Car:
  speed=0
  def upSpeed(self,value):
    self.speed+=value
    print("The current speed of Car is %d "%self.speed)

class Sedan(Car):
  def upSpeed(self, value):
      self.speed+=value
      if self.speed>150:
        self.speed=150
        print("The current speed of Car is %d "% self.speed)
class Truck(Car):
  pass

sedan1,Truck1=None,None
Truck1=Truck()
sedan1=Sedan()
print("Truck -->",end="")
Truck1.speed(150)
print("Sedan -->",end="")
sedan1.speed(200)