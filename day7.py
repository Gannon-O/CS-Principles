# This file was created by: Gannon O'Leary
import random 
# we define a function with a parameter called greeting
def randomPicker ():
    # get names
    nameList = []
    # getting names from user
    x = input ('give a name...')
    # add the name to this list
    nameList.append(x)
    y = input ('give a name...')
    nameList.append(y)
    z = input ('give a name...')
    nameList.append(z)
    print(nameList)
    # choose a name from appended list
    randName = random.choice(nameList) 
    # return that name from the function 
    return randName
    print(x)
    print(y)
    print(z)
    
    print(randomPicker())    
