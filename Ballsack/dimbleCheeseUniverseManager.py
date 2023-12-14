import os



def sparkplug():
    tempDir=os.getcwd()
    DirectorySaveFileList = (tempDir+"\\Ballsack\\assets\\universe.txt")
    with open(DirectorySaveFileList,"r") as UniverseFile:
        tempArray = {}
        for i in range(0,len(UniverseFile.readlines())):
            tempArray[i] = str(UniverseFile.readlines())
        ArrayWithInformation = tempArray[0].split("-")
    print(ArrayWithInformation[1])


class Character:
    def __init__(self):
        pass



sparkplug()