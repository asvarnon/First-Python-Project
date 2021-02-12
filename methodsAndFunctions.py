# def helloPerson(name):
#     print(f"Hello {name}")

# def addNumbers(a, b):
#     return a + b

# def squareAddedNum(num):
#     return num**2


# addedNumber = addNumbers(2, 4)
# print(squareAddedNum(addedNumber))

def createFile():
    # windowsFile = open("Desktop", "w")
    macFile = open("/Users/austinvarnon/Desktop/testing.txt", "w")
    macFile.write("Hi \n")
    macFile.writelines("lololol...")
    macFile.close()
    
createFile()