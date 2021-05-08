class superClass:
  def method(self):
    pass

class subClass1(superClass):
  def method(self):
    print("subClass method overriding!")

class subClass2(subClass1):
  pass

sub1=subClass1()
sub2=subClass2()
# superclass=superClass()
sub1.method()
# sub2.method()
# superclass.method()   