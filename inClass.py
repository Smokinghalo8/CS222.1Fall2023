def mainTemp1():
    for n in range(10):
        print("BSU")
        if n == 5:
            break   #This statment will stop the loop dead in their tracks


def mainTemp2():
    for x in range(3):
        for y in range(2):
            #print("bsu")
            if y==2 or x==2:
                continue
            print("BSU")


def mainTemp3(fah):
    return (fah-32)*5.0 / 9.0
#print(mainTemp3(50))

def Year(credits=0):    #Putting the '=0' to the end of credits get overwritten when saying an argument later in the code
    if(credits>=90):
        return("Senior")
    elif(credits>=60):
        return("Junior")
    elif(credits>=30):
        return("Sophmore")
    elif(credits>=0 and credits<30):
        return("Freshman")
    else:
        return("Error code 1 - error in 'Year' function")
    
#print(Year(30))

def deafaultOp(x=0,y=0,z=0):
    print(f"x={x}y={y}z={z}")

def main():
    midterm = [70,92,100]
    try:
        print(midterm[2])   #bad exception
    except:     #Try Catch command
        print("Error 1 - error in main function, overflow of index")
    x=0
    try:
        z=10/x
    except:
        print("Error 2 - Error in main function, divide by zero error")
main()