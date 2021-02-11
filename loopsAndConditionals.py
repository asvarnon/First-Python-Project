# randomNumber = 2

# if randomNumber:
#     print('ITS TRUE')
# else:
#     print('ITS FALSE')


#Conditionals
# name = "Austin"
# if name == "Frankie":
#     print(f"Hello {name}!")
# elif name == "Austin":
#     print(f"Hello {name}!")
# else:
#     print("What is your name?")

#For loops
# myNames = ['Austin','Frankie','Clayton']
# for name in myNames:
#     if name == "Frankie":
#         print(f"Hello {name}!")
#     elif name == "Austin":
#         print(f"Hello {name}!")
#     else:
#         print("What is your name?")

# myNumbers = [1,2,3,4,5,6,7,8,9,10,11,12]
# for num in myNumbers:
#     if num % 2 ==0:
#         print(num)

# listSum = 0
# for num in myNumbers:
#     listSum = listSum + num
# print(listSum)

# myString = "Hello World"
# for letter in myString:
#     print(letter)


#--------------TUPLES-------------------
# myList = [(1,2),(3,4),(5,6),(7,8)]
# print(len(myList))
#Tuple unpacking-----
# for a,b in myList:
#     print(a)
#     print(b)

# myList = [(1,2,3),(4,5,6),(7,8,9)]
# for a,b,c in myList:
#     print(b)

#---------------Dictionaries----------------
# d = {'key1':1, 'key2':2, 'key3':3}
# #default iterates through keys
# for key,value in d.items():
#     print(value)
#     print(key)


#---------------While Loops-------------
# x = 0
# while x < 5:
#     print(f"the current value is: {x}")
#     x += 1
# else:
#     print('x is not less than 5')    

#break, continue, pass
# x = [1,2,3]
# myString = "Austin"

# for item in x:

#     pass
# print('end of script')

# for letter in myString:
#     if letter == 'A':
#         continue
#     print(letter)

# for letter in myString:
#     if letter == 't':
#         break
#     print(letter)


#------------useful operators-----------
##  RANGE
# myList = [1,2,3,4,5,6,7,8,9]
# range(start, stop, step)
# range(if single number then 0 to that number)
# for num in range(3,9,2):
#     print(num)
# print(list(range(3, 9, 2)))

##  ENUMERATE
# indexCount = 0
# word = 'abcdef'
# for letter,index in enumerate(word):
#     print(letter)
#     print(index)
#     print('\n')


##  ZIP
# myList1 = [1,2,3,4,5]
# myList2 = ['a','b','c','d','e']
# myList3 = [100, 200, 300]

# for item in zip(myList1, myList2, myList3):  
#     print(item)
# print(list(zip(myList1, myList2, myList3)))

##  IN
# print('x' in [1,2,3])
# print('x' in ['x', 'y', 'z'])

# d = {'key1':345}
# print(345 in d.values())
# print('key1' in d.keys())

## MIN, MAX
# myList1 = [1,2,3,4,5]
# print(min(myList1))
# print(max(myList1))

## RANDOM, SHUFFLE
# from random import shuffle
# myList = [1,2,3,4,5,6]
# shuffle(myList)
# print(myList)
# from random import randint
# print(randint(1,100))

## INPUT
# myNumber = input('Enter a number: ')
# print(type(myNumber))
# print(type(float(myNumber)))
# print(f'The number you chose is: {myNumber}')


#----------------------LIST COMPREHENSION-----------------------

# myString = 'hello'
# myList = []
# for letter in myString:
#     myList.append(letter)
# print(myList)

## OOOORRRRR

# myString = 'hello'
# myNums = '1234'
# myList = [letter for letter in myString]
# print(myList)
# myNums = [x for x in myNums]
# print(myNums)

##RANDOM LIST GENERATION SCRIPT
# myList = [x for x in range(1,10)]
# print(myList)

# myOtherList = [x for x in range(1,11) if x%2 ==0]
# print(myOtherList)

# celcius = [0,10,20,30,34.4]
# fahrenheit = [( (9/5)*temp + 32) for temp in celcius]
# print(fahrenheit)

#Nested loop
# myList = []
# for x in [2,4,6]:
#     for y in [100,200,300]:
#         myList.append(x*y)
# print(set(myList))

##Also like:
# myList = [x*y*z for x in [2,4,6] for y in [1,10,100] for z in [.1,.2,.3]]
# print(myList)



##---------------------ASSESSMENT SOLUTIONS-------------------
##1)
# st = 'Print only the words that start with s in this sentence'
# print(st.split())
# for word in st.split():
#     if word[0] == 's':
#         print(word)


##3)
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
# myList = [x for x in range(1,50) if x%3 == 0]
# print(myList)

##4)
# st = 'Print every word in this sentence that has an even number of letters'
# for word in st.split():
#     if len(word)%2 == 0:
#         print(word)

##5)
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for num in range(1,101):
    if num%3 == 0:
        print(num, 'Fizz')
    if num%5 == 0:
        print(num, 'Buzz')
    if num%3 == 0 and num%5 == 0:
        print(num, 'FizzBuzz')


##6)
st = 'Create a list of the first letters of every word in this string'
myList =[word[0] for word in st.split()]
print(myList)



















