def main():
    print("Welcome to CS222!")
    firstName = input(print("Please type in your first name? "))
    print("Welcome "+firstName)
    payRate = float(input("Please type in your hourly play? "))
    hoursWorked = float(input("How many hours did you work? "))
    number = float(payRate*hoursWorked)
    print("$"+str(payRate+hoursWorked))
    print("The rounded amount is: "+round(number))
    n = float(payRate*hoursWorked)
    guessedNumber = float(input("Say a number lower than that!"))

    if guessedNumber>n:
        print("higher")
    elif guessedNumber<n:
        print("lower")
    else:
        print("Exact")


    for counter in range(5):        #This is a basic for loop, counter is defined in the for and amount of passes are in the range, it starts at 0 and ends at 5
        print(counter)

main()
