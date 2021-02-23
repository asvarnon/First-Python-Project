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
print(list(map(lambda x : x[::-1], names)))

