


def square(x):
    return x**2


numbers = [1,2,3,4,5]
squares = map(square,numbers)   #This will use the function 'square' on every number in the list 'numbers'
squaresList = list(squares)
print(squaresList)



fruits = ["apple","bannana","cherry"]
wordLenghts = list(map(len,fruits))
print(wordLenghts)



def ConvertToUpper(str):
    return str.upper()

names = ["alice","bob","carol","dave","eve"]
namesBetter=print(list(map(ConvertToUpper,names)))


def FahToCel(fah):
    return((fah-32)*5.0/9.0)
celsiousTemp = [212,32,100]
farihnheightTemp=print(list(map(FahToCel,celsiousTemp)))