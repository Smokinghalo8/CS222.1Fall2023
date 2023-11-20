import os



def sparkplug():
    tempDir=os.getcwd()
    DirectorySaveFileList = (tempDir+"\\Ballsack\\assets\\universe.txt")
    print(DirectorySaveFileList)
    with open(DirectorySaveFileList,"r") as UniverseFile:
        LinesOfFile = str(UniverseFile.readlines())
        ArrayWithInformation = LinesOfFile.split("-")
    print()



class Character:
    def __init__(self):
        pass



sparkplug()