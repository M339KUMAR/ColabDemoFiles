
class Person():

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def speak(self, name, age):
        print(f"Hi {self.name} Hello:")

    def walk(self):
        print(f"Hi {self.name} is walking:")

    def eat(self, name, age):
        print(f"Hi {self.name} is Eating:")

    def sleep(self, name, age):
        print(f"Hi {self.name} is Sleeping:")

    #def main():
bob=Person('bob',25)#----->works
tom=Person('tom',35)#----->works
#bob=Person()-------->Not Work
#tom=Person()-------->Not Work
if __name__=="__main__":
   print(f"Running {bob.__class__.__name__}")
   bob.speak('bob', 25)
   tom.speak('tom', 35)
   bob.walk()
   tom.walk()
