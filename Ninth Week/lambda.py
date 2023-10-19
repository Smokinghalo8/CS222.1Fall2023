#anonomous function - does not have a name as a function - and only one to two lines

add = lambda x, y: x + y        #This is the function - add is the function - the two arguments are before the : and the text after is the function
result = add(3,5)

print(result)


numbers = [1,2,3,4,5]
squareNumbers = print(list(map(lambda x: x**2, numbers)))   #Didnt give it a name- the lambda function

fahTemps=[212,32,100]
celsTemps = print(list(map(lambda f: (f-32)*5.0/9.0, fahTemps)))

numbers = [3,1,4,1,5,9,2,6,5,3,5]
sortedNumbers = sorted(numbers) #Ascending
sortedNumbers2=sorted(numbers, reverse=True)
print(sortedNumbers)



midterm = {'Carol':92,'Alice':95,'Bob':88,'Dave':90,'Eve':100}
sortedScores = sorted(midterm.items(),key=lambda item: item[1])  #Lambda function in this case sorts the list by the values not the keys!
#Sorted by the Key not the value - the names not the numbers    #.items() gives both keys and values!
print(sortedScores)



points = [(1,3,10), (2,1,20), (4,2,15)]
sortedPoints = print(sorted(points,key=lambda x: x[2], ))