import sqlite3

conn = sqlite3.connect(r'D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\Database\univ.db')

cur = conn.cursor()

# cur.execute('create table Dept(deptno integer primary key,name text)')
# cur.execute('create table Students(roll integer primary key,name text,city text,deptno integer,foreign key(deptno) references Dept(deptno))')
# cur.execute('insert into Dept values(10,"CSE")')

# deptno = int(input("Enter Dept Number : "))
# deptname = input("Enter Dept Name : ")

# cur.execute(f'insert into Dept values({deptno},"{deptname}")')          # Inserting values through user.

# for i in range(15):
#     studentRoll_no = int(input("Enter Student Roll Number : "))
#     studentName = input("Enter Student Name : ")
#     studentCity = input("Enter Student City : ")
#     studentDeptNO = input("Enter Student Dept No : ")
#     cur.execute(f'insert into Students values({studentRoll_no},"{studentName}","{studentCity}",{studentDeptNO})')

# Select Query : 

# row = cur.execute('select * from dept')
# row = cur.execute('select name from students')
# print(row.fetchone())       # we will get only one row
# print(row.fetchmany(3))     # we will get how many rows we write.
# print(row.fetchall())       # we will get all the rows.

# row = cur.execute('select distinct(name) from students')    # Distinct

# row = cur.execute('select name from students where city = "Delhi"')
# row = cur.execute('select name from students where name Like "A%"') # Names start with 'A'.
# row = cur.execute('select name from students where name Like "A%"') # Names start with 'A'.
#row = cur.execute('select name from students where name Like "%A"') # Names start with 'A'.
# #-------------------------
# lst = row.fetchall()

# for i in lst:
#     print(i[0])
# #-------------------------
# row = cur.execute('select roll,name from students where city not in ("Delhi","Hyderabad")') # Names start with 'A'.
# print(row.fetchall())

# row = cur.execute('''select roll,students.name,Dept.name
#                         from Students,Dept
#                         where Students.deptno = Dept.deptno''')

# #-------------------------
# lst = row.fetchall()

# for i in lst:
#     print(i)
# #-------------------------

# row = cur.execute("select city,count(*) from Students group by city")
# row = cur.execute("select city,count(*) from Students group by city having count(*) > 2")
row = cur.execute("select name from Students where city in (select city from Students where name = 'Verma')")

#-------------------------
lst = row.fetchall()

for i in lst:
    print(i)
#-------------------------

conn.commit()
cur.close()
conn.close()