#map and filter functions
# def square(num):
#     return num**2

myNums = [1,2,3,4,5]

# for item in map(square, myNums):
#     print(item)

# print(list(map(square, myNums)))

def splicer(str):
    if len(str) % 2 == 0:
        return 'EVEN'
    else:
        return str[0]

names = ['Andy', 'Eve', 'Sally']

# print(list(map(splicer, names)))

def checkEven(num):
    return num % 2 == 0

myNumArr = [1,2,3,4,5,6]

# print(list(filter(checkEven, myNumArr)))

#turning square function into lambda expression
def square(num):
    return num**2

# lambda num: num ** 2
#can assign but really works well with map/filter
square = lambda num: num ** 2

# print(list(map(lambda num: num ** 2, myNumArr)))
# print(list(map(lambda x : x[::-1], names)))

################### PRACTICE / HW Problems ##################
import math as math

def vol(radius):
    return ((4/3)*math.pi*radius**3)

# print(vol(2))

#Check if a number is in a range or no
def rangeCheck(num, low, high):
    if num in range(low, high):
        return True
    else:
        return False

# print(rangeCheck(3, 1, 10))

#accepts string and calculates the number of uppercase and lowercase letters
def upLow(str):
    upperCount = 0
    lowerCount = 0
    for char in str:
        if char.isupper():
            upperCount += 1
        else:
            lowerCount += 1   
    return upperCount, lowerCount

# print(upLow("Hi, my name is Austin"))

#takes in a list and returns a list with unique elements of the first list
def uniqueElements(lst):
    return list(set(lst))

# print(uniqueElements([1,1,1,2,2,2,3,3,3,4,4,4]))

#multiply all numbers in a list
def multiply(numbers):
    multipliedNumber = 1
    for num in numbers:
        multipliedNumber *= num
    return multipliedNumber

# print(multiply([1,2,3,4,5]))

#check if string is palindrome
def isPal(str):
    splitString = [char for char in str]
    reversedList = splitString[::-1]
    if str == ''.join(reversedList):
        return True
    else:
        return False

    

print(isPal("racecar"))
print(isPal("hello"))
print(isPal('91019'))