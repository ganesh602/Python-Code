students = {}
for i in range(5):
    rollNo = int(input("Enter Roll No. : "))
    Name = input("Enter Name : ")
    Dept_name = input("Enter Dept Name : ")
    temp = {}
    # # any way we can give the value as Dictionary.
    # temp['RollNo'] = rollNo
    # temp['Name'] = Name
    # temp['Dept_Name'] = Dept_name

    # students[Name] = temp
    students[Name] = {'Roll': rollNo,'Name': Name,'Dept_Name':Dept_name}

print(students)