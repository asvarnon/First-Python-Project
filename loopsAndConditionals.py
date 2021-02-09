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
x = [1,2,3]
myString = "Austin"

# for item in x:

#     pass
# print('end of script')

for letter in myString:
    if letter == 'A':
        continue
    print(letter)

for letter in myString:
    if letter == 't':
        break
    print(letter)

