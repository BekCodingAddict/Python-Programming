import time
import threading
import multiprocessing

class RacingCar:
  carName=""
  def __init__(self,name):
    self.carName=name

  def runCar(self):
    for _ in range(0,3):
      carStr=self.carName+"--going foward!\n"
      print(carStr, end=" ")
      time.sleep(0.3)


car1=RacingCar("Car1")
car2=RacingCar("Car2")
car3=RacingCar("Car3")

# car1.runCar()
# car2.runCar()
# # car3.runCar()
# tr1=threading.Thread(target=car1.runCar())
# tr2=threading.Thread(target=car2.runCar())
# tr3=threading.Thread(target=car3.runCar())
# tr1.start();tr2.start();tr3.start()

mp1=multiprocessing.Process(target=car1.runCar())
mp2=multiprocessing.Process(target=car2.runCar())
mp3=multiprocessing.Process(target=car3.runCar())
mp1.start();mp2.start();mp3.start()
mp1.join();mp2.join();mp3.join()