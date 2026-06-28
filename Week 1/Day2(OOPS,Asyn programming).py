# Class

# class Person:
#     def __init__(self, name, age):
#        self.name = name
#        self.age =age

# person1 =Person("Nouman",32)

# print(person1.name)
# print(person1.age)

# Inheritance 

# class specie :
#     def __init__(self,name,age):
#      self.name = name
#      self.age = age

#     def barks(self):
#      print("Dog barks")

# class Dog(specie):
#     def __init__(self,name,age,breed):
#        self.name=name
#        self.age=age
#        self.breed=breed

#     def night(self):
#        print("Dog barks at night")

# D = specie("Shaepard",2)
# D = Dog("Lebra",3,"Ousto")

# D.barks()
# D.night()

# Method Overriding

class Animals:
    def __init__(self,name):
        self.name= name
        
    def sound(self):
        print("Barks")

class Dog(Animals):  # always exucute child class function because it uses MRO
    def sound(self):
        print("Barks")

D = Animals("Lebra")
D= Dog("lebra")

D.sound()