myIncome = 100
taxRate = 0.1
taxes = myIncome*taxRate

# print(type(taxes))
# print(taxes)

# randomString = "Hi how are you"
# print(len(randomString))


# print(
#     randomString[0],
#     randomString[0:3]
# )
# print(
#     randomString[7:]   
# )

# result = 100/777
# print("This result was:{r}".format(r=result))
# print("This result was: {r:1.6f}".format(r=result))


# newList = [1, 2, 3, 4, 5]
# print(newList)
# newList.append(6)
# print(newList)
# newList.pop()
# print(newList)

# poppedItem = newList.pop(3)
# print(poppedItem)

# myDict = {'key1':'val1', 'key2':'val2'}
# print(myDict['key2'])

# priceLookUp = {'apple':2.99, 'oranges':3.99, 'milk':1.99}
# print(priceLookUp['oranges' ])


#Key within a key
    # d={'k1':123, 'k2':['a','b','c'], 'k3':{'insideKey':100}}
    # print(d['k2'])

#stacking key calls
    # print(d['k2'][2])
    # print(d['k3']['insideKey'])
    # print(d['k2'][0].upper())

#Appending and changing key values
    # d['k1'] = 'NEW VALUE'
    # d['k4'] = 9000
    # print(d)

# print(d.keys())
# print(d.values())
# print(d.items())

#Tuples
# t = (1,3,3)
# print(type(t))
# length = len(t)
# print(f"Length of t: {length}")
# count = t.count(3)
# print(f"Number of times 3 comes up: {count} times")



#Sets
# mySet = set()
# mySet.add(1)
# mySet.add(2)
# print(mySet)
# myList = [1,1,1,2,2,2,3,3,3,3,3]
# print(set(myList))

# myFile = open('/Users/austinvarnon/Python Projects/First python project/exampleFile.txt')
# myFile = open('exampleFile.txt')
# myFile.readlines()
# myFile.close()

# #OR
# with open('exampleFile.txt') as myNewFile:
#     contents = myNewFile.readlines


#Mode variables are:
# mode='r' = is read only
# mode='w' = write only (will overwrite files or create new!)
# mode='a' = is append only (add on to files)
# mode='r+' = is reading and writing
# mode='w+' = is writing and reading


# with open("exampleFile.txt",mode='a') as myFile:
#     myFile.write("\nFourth line")

# with open("exampleFile.txt",mode='w') as myFile:
#     myFile.write("I CREATED THIS FILE")

# with open("exampleFile.txt",mode='r') as myFile:
#     contents = myFile.read()
#     print(contents)


# -----------------ASSESSMENT NOTES/PROBLEMS----------------------------
import math
#NOTE: LISTS (Arrays), TUPLES (like FINAL, immutable), DICTIONARIES (hashmaps with key value pairs), SET(unique objects, no duplicates.)

# print(type(3 + 1.5 + 4))

# print(math.sqrt(25))
# print(5**2)

# s = 'hello'
# # Print out 'e' using indexing
# print(s[1])

#------------GOOD TO REMEMBER TO REVERSE A STRING (variable)[::-1]
# print(s[::-1])

# list3 = [1,2,[3,4,'hello']]
# list3[2][2] = 'goodbye'
# print(list3)

# d = {'simple_key':'hello'}
# # Grab 'hello'
# print(d['simple_key'])

# d = {'k1':{'k2':'hello'}}
# # Grab 'hello'
# print(d['k1']['k2'])

# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# #Grab hello
# #tricky
# print(d['k1'][0]['nest_key'][1][0])

# list5 = [1,2,2,33,4,4,11,22,3,3,2]
# print(set(list5))


# print("1:", 2 > 3)
# print("2:", 3 <= 2)
# print("3:", 3 ==2.0)
# print("4:", 3.0 == 3)
# print("5:", 4**0.5 != 2)

#Chaining comparison operators.
# and, or, not

print(2 == 2 and 3 == 3)




