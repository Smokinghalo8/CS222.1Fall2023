def part1():
    #Error 1 - Error is BMI Grading Scale
    #BMI = (weight * 703) / (height)2
    #optimal if his or her BMI is between 18.5 and 25.
    #If the BMI is less than 18.5, the person is considered to be underweight.
    #If the BMI value is greater than 25, the person is considered to be overweight.
    weight = int(input(print("How Much Do You Weigh? ")))
    height = int(input(print("How Tall Are You in inches? ")))
    BMI = (weight*703)/height**2
    #BMI = float(((weight*703)/(height*height)))#I cannot find the squared operator
    print(f"Your BMI Is: {BMI}")
    if BMI>=25.1:
        print("You Are Overweight :c )")
    elif BMI<=18.4:
        print("You Are Underwight :c )")
    elif BMI>=18.5 & BMI<=15:
        print("You are Optimal :p ")
    else:
        print("Error 1")

#Write a program that uses a loop to compute and print the sum of all even numbers between 2 and 100 (inclusive).

def part2():
    tempnumber1 = 0
    for number in range(0,100): #Does it include the 100? if so Change the 100 in the range to 101!
        if(number%2==0):
            print(f"TempNumber: {tempnumber1} - Number: {number}")
            tempnumber1+=number
    print(f"Number: {tempnumber1}")


#Write a program that uses a loop to compute and print the sum of all odd numbers between a and b (inclusive), where a and b are entered by the user.

def part3():
    tempnumber1 = 0
    userInput1 = int(input(print("Starting Number: ")))
    userInput2 = int(input(print("Ending Number: ")))
    for number in range(userInput1, userInput2):
        if(number%2==1):        #Negative Statements in Python are denoted by the word 'not' NOT '!'!
            print(f"TempNumber: {tempnumber1} - Number: {number}")
            tempnumber1+=number
    print(f"Final Number: {tempnumber1}")

#Your company has shares of stock it would like to sell when their value exceeds a certain target price. 
# Write a program that reads the target price and then reads the current stock price until it is at least the target price. 
# Your program should read a sequence of floating-point values from standard input.         what
# Upon reaching or exceeding the target price, your program should output a message that says "Shares can be sold now".


# Your program should read a sequence of floating-point values from standard input. 
# ^^ Does this mean an array or user input???


def part4():
    CurrentValue=0
    targetValue = int(input(print("Target Price: ")))
    while CurrentValue<targetValue:
        CurrentValue = int(input(print("Current Price: ")))
    print(f"Shares can now be sold! Current Price: {CurrentValue} Target Price: {targetValue}")


def part4m2():
    curr=[17,29,39,10,46,103,28,183]
    target = int(input(print("Target Price: ")))
    for n in curr:
        if n >=target:
            print(f"Shares can now be sold! Current Price: {curr} Target Price: {target}")
        else:
            print(f"Shares Cannot be Sold, Changing number; Currect Number in Curr: {n}")



#At one college, the tuition for a full-time student is $8,000 per semester.
#It has been announced that the tuition will increase by 3 percent each year for the next 5 years.
# Write a program with a loop that displays the projected semester tuition amount for each of the next 5 years.


def part5():
    startingTuitionSemester = 8000
    endAmount = 0
    for n in range(0,10): #should be 10 passes
            if(n%2==0 and n!=0):
                #print(f"Going through the reminder flag pass: {n}") #debugFlag
                startingTuitionSemester = startingTuitionSemester*1.003
            endAmount +=startingTuitionSemester
            #print(f"Pass Number: {n} Amount of money ended Right Now: {endAmount}")
            print(f"Semester Number: {n} Price so far: {endAmount}")




