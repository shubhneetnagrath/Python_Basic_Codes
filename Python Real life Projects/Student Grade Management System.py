StudentName =["Shubhneet","Vihaan","Gaurav","Sumit","Raj"]
StudentMarks = [78,89,56,98,91]
print(StudentName)
print(StudentMarks)
#Changed Vihaan's marks from 89 to 67.
StudentMarks[1] = 67
print(StudentName)
print(StudentMarks)
#Addition of a student
StudentName.append("Vijay")
StudentMarks.append(83)
print(StudentName)
print(StudentMarks)
#Remove a student
StudentName.remove("Vijay")
StudentMarks.remove(83)
print(StudentName)
print(StudentMarks)
#Show Topper
Highest = max(StudentMarks)
index = StudentMarks.index(Highest)

print("Topper:",StudentName[index])
print("Marks:",Highest)

def average():
    avg = sum(StudentMarks) / len(StudentMarks)
    print("Average:", avg)

average()



