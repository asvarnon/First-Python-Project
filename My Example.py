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
myList = [1,1,1,2,2,2,3,3,3,3,3]
print(set(myList))



