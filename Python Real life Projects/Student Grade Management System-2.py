StudentName =["Shubhneet","Vihaan","Gaurav","Sumit","Raj"]
StudentMarks = [78,89,56,98,91]

def showStudents():
    for i in range(len(StudentName)):
        print(StudentName[i],"-",StudentMarks[i])

def updateMarks():
    StudentMarks[1] = 67

def addStudent():
    StudentName.append("Vijay")
    StudentMarks.append(83)

def removeStudent():
    index = StudentName.index("Vijay")
    StudentName.remove("Vijay")
    StudentMarks.pop(index)

def showTopper():
    Highest = max(StudentMarks)
    index = StudentMarks.index(Highest)
    print("Topper:",StudentName[index],"-",Highest)

def average():
    avg = sum(StudentMarks) / len(StudentMarks)
    print("Average:", avg)

showStudents()
updateMarks()
addStudent()
removeStudent()
showTopper()
average()