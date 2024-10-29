# this file was created by: Gannon O'Leary
from time import sleep

i = 1
while i < 11:
  print("Bueller")
  if i == 10:
    break
  i += 1
names = ["Anyone", "bob","joe"]
for i in names:
    # x = input("give me another name")
    # names.append(x)
    print(i)
    sleep(1)


def myfunc(message):
    name = input("give me name")
    print(message + name)

askingforname = True

names = 0

while askingforname:
    myfunc("hello there... ")
    names += 1
    if names > 5:
        askingforname = False