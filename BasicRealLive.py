def main():
    for i in range(0,5,2):        #You only need to add the base argument in range when you do not start from 0! Arguments go like: {Starting Place, Ending Place, Integers per step}
        print(f"Hello {i}")     #Add the little f before the starting phrase and curly brace the variable!

def main2():
    numbers = [7, 5, 19, 3]     #You can make a list of anything!
    for number in numbers:
        print(number)

    print()

    total = 0
    for number in numbers:
        total += number
    print(total)


    names = ["Alice", "Bob", "Carol", "Dave", "Eve"]
    for name in names:
        print(name)

def main3():
    
    #numbers2 = [7,5,19,3]
    #print(numbers2[2])#Prints out the 3rd item from the list
    #for i in range(0,len(numbers2)):    #len is the length command
    #    print(numbers2[i])

    #for x in range(0,5):
    #    for y in range(0,3):
    #        print(f"CS222! {x} - {y}")

    #for i in range(0,4):
    #    print(f"Outer Loop {i}")
    #    for j in range(0,3):
    #        print(f"Inner Loop {j}")

    #for counter in range(0,10):
    #    if(counter % 2 ==0):        #Checks to see if the number if even!
    #        print(f"Counter: {counter}")

    #footballTeams = ["colts","titans","texans","carps"]
    #print(len(footballTeams))
    #print(len(footballTeams[2]))       #Grabbing the lenght of the string - a string is just a list of characters put together
    #print(footballTeams[3][2])      #Taking apart the string to get the characters by themselves!


    #exams = [[72,82,93], [100,92,97], [50,90,80]]   #Each list is a list of student scores on exams!
    #for exam in exams:
    #    for score in exam:
    #        if(score >=60):
    #            print(score)


    x=10
    y=5
    if x>0 or y!=2:
        print("Hello!")
    else:
        print("World!")

main3()