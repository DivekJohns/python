class myClass():
  def method1(self):
      print("method1")
        
  def method2(self,someString):    
      print("Software Testing:" + someString)



class childClass(myClass):
  def method1(self):
       myClass.method1(self)
        
  def method2(self, str):
        myClass.method2(self,str)   


c = childClass ()
c.method1()
c.method2(" Testing is fun")


class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Welcome to universe, " + self.name)

User1 = User("Divek")
User1.sayHello()