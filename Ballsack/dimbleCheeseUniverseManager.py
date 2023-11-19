import os



def sparkplug():
    tempDir=os.getcwd()
    DirectorySaveFileList = os.listdir(tempDir+"\Ballsack\assets\universe.txt")
    file1 = open(DirectorySaveFileList,"r")
    print(file1.read())

sparkplug()