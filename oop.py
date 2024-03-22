
class Person:
    def __init__ (self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def introduce(self):
        print("Hello, My name is",self.name,".\nI am ",self.age," years old and I am a ",self.gender,".\nThank you!" )


p = Person("James", 22 , "Male" )
p.introduce()




