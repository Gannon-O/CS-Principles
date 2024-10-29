import pygame
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Gannon", 15)
p2 = Person("Omer", 15)
p3 = Person("Joaquin", 15)


print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
print(p3.name)
print(p3.age)
