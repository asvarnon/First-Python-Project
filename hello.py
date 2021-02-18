def createFile():
    windowsFile = open("E:\\Hello.txt", "w")
    windowsFile.write('Hi \n')
    windowsFile.close()
    # macFile = open("/Users/austinvarnon/Desktop/testing.txt", "w")
    # macFile.write("Hi \n")
    # macFile.writelines("lololol...")
    # macFile.close()
    
createFile()