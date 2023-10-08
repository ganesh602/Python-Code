import sqlite3

conn = sqlite3.connect(r"D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\Database\univ.db")

cur = conn.cursor()

# cur.execute(''' update dept
#                 set name = 'Chem'
#                 where name = 'Mech' ''')

# cur.execute(''' update students
#                 set city = 'Bhopali'
#                 where roll = 15 ''')

# cur.execute("delete from Students where roll = 15")
# cur.execute("delete from Dept where deptno = 40")

# row = cur.execute("select * from dept")
row = cur.execute("select * from students")

lst = row.fetchall()

for i in lst:
    print(i)
    

conn.commit()
cur.close()
conn.close()
