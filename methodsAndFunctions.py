def helloPerson(name):
    print(f"Hello {name}")

def addNumbers(a, b):
    return a + b

def squareAddedNum(num):
    return num**2

def evenCheck(num):
    return num % 2 == 0


# if you put false instead of pass, it will cancel after 1 number, not go through them.
def checkEvenList(numList):
    #return all even numbers in a list.
    evenNumbers = []
    for number in numList:
        if number % 2 == 0:
            evenNumbers.append(number)
        else:
            pass

    return evenNumbers

numList = [1,2,3,4,5]
# print(type(checkEvenList(numList)))
# print(checkEvenList(numList))
# addedNumber = addNumbers(2, 4)
# print(squareAddedNum(addedNumber))


workHours = [('Abby',100),('Billy',4000),('Cassie',800)]
def employeeCheck(workHours):
    currentMax = 0.0
    employeeOfTheMonth = ''

    for employee,hours in workHours:
        if hours > currentMax:
            currentMax = hours
            employeeOfTheMonth = employee
        else:
            pass

    #returning a tuple
    return (employeeOfTheMonth,currentMax)

# print(employeeCheck(workHours))

#unpack tuples with function call
name,hours = employeeCheck(workHours)
# print(employeeCheck(workHours))
# print(name)
# print(hours)

##########################################################################################
from random import shuffle
example = [1,2,3,4,5,6,7]

#INITIAL LIST
myList = [' ', '0', ' ']

#SHUFFLE LIST
def shuffleList(myList):
    shuffle(myList)
    return myList
# print(shuffleList(myList))

#USER GUESS
def playerGuess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input('pick a number of 0, 1, 2 \n')
    return int(guess)

# print(f"Your guess is {playerGuess()}")

#CHECK GUESS
def checkGuess(aList, guess):
    if aList[guess] == '0':
        print("Correct!")
    else:
        print("Wrong Guess")
        print(aList)

# checkGuess(myList, playerGuess())
#adding comment to make sure windows remote

##########################################################################################

# def myFunc(a, b, c = 0, d = 0, e = 0):
#     #returns 5% of the sum of a and b
#     return sum((a, b, c, d, e)) * 0.05

#can only take 2-5 params
# print(myFunc(2,4))


def myFunct(*args):
    return sum(args) * 0.05

# the '*' allows unlimited amount of params by returning them in a tuple
# print(myFunct(2, 3))
# print(myFunct(2,4.6,6,4))

def myFunction(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print(' I did not find any fruit here..')

# '**' returns a dictionary
# print(myFunction(fruit = 'apple', veggie = 'lettuce'))


def myFunctions(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))

# print(myFunctions(10, 20, 30, fruit='orange', food='eggs', animal='dog')
# )

def myfunc(String):
    newString = ""
    for position, letter in enumerate(String):
        # print(f'Begin of loop, char is {letter} and the new quote is {newString}')
        if (position +1 ) % 2 == 0:
            # print('UPPER')
            newString += letter.upper()
        else:
            # print('LOWER')
            newString += letter.lower()
        # print(f"\nAfter Loop, new quote is {newString}\n")
    return newString

# print(myfunc("Anthropomorphism"))

#given an integer, returns true if within 10 of either 100 or 200
def almostThere(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

# print(almostThere(103))
# print(almostThere(150))

#Find 33
def has33(nums):
    numberCount = 0
    for num in range(0, len(nums) - 1):
        if nums[num] == 3 and nums[num + 1] == 3:
            return True
    return False

# print(has33([1,3,3]))

#given a string, return a string where for every character in the original, there are 3 chars
def paperDoll(str):
    result = ''
    for char in str:
        result += char*3
    return result

# print(paperDoll("hello"))

#blackjack
def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a, b, c]) - 10 
    else:
        return "BUST"

# print(blackjack(2,10,10))
# print(blackjack(2,10,11))

#Return sum of numbers in array, except ignore sections with a 6 and extending to the next 9. return 0 for no numbers.
def summer69(array):
    total = 0
    add = True
    for num in array:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

# print(summer69([1,3,5]))
# print(summer69([1,3,6,9]))
# print(summer69([1,3,6,7,8,9]))

#function returns true if it contains 007 in order. does not have to be consecutively.
def spyGame(nums):

    codeList = [0, 0, 7, 'x']

    for num in nums:
        if num == codeList[0]:
            codeList.pop(0)
    return len(codeList) == 1

# print(spyGame([1,2,4,0,0,7,5]))
# print(spyGame([1,2,0,4,0,5,6,7]))
# print(spyGame([1,7,2,4,0,0,5]))

#Counting primes
def countPrimes(num):
    #check for 0 or 1 input
    if num < 2:
        return 0
    # 2 or greater

    #store prime numbers
    primes = [2]
    #counter going up to the input num
    x = 3

    #x is going through every number to input num
    while x <= num:
        #check if x in prime
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    print(len(primes))
    return len(primes)

# countPrimes(100)

