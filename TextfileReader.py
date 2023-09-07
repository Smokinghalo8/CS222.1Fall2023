def main():
    try:
        #open function - built in - will open a file
        studentlist1 = open("text.txt", 'r')   #r meaning 'read' mode

        students = studentlist1.readlines()

        studentlist1.close()
        #print(students)
        for s in students:
            tempS = s.split()   #by default splits a string between spaces
            print(tempS[0])
    except FileNotFoundError:
        print("Error 1 - filenotFound error")
main()