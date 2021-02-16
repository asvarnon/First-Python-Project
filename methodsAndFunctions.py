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
print(checkEvenList(numList))
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

print(employeeCheck(workHours))

#unpack tuples with function call
name,hours,location = employeeCheck(workHours)
print(name)
print(hours)











# def createFile():
#     # windowsFile = open("Desktop", "w")
#     macFile = open("/Users/austinvarnon/Desktop/testing.txt", "w")
#     macFile.write("Hi \n")
#     macFile.writelines("lololol...")
#     macFile.close()
    
# createFile()


