import sqlite3

conn = sqlite3.connect(r"D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\Database\Shop.db")

cur = conn.cursor()

# cur.execute(''' create table Customer
#                     (
#                         Custid integer primary key,
#                         Cname text,
#                         Address text
#                     )   
#                   ''')

# cur.execute(''' create table Product
#                     (
#                         ProdNo integer primary key,
#                         Pname text,
#                         Price float
#                     )   
#                   ''')

# Enable foreign key support
cur.execute("PRAGMA foreign_keys = ON")

# cur.execute(''' create table Orders
#                     (
#                         OrderNo integer,
#                         Custid integer,
#                         ProdNo integer,
#                         Qty integer,
#                         foreign key(Custid) references Customer(Custid),
#                         foreign key(ProdNo) references Product(ProdNo)
#                     )   
#                   ''')

# cur.execute('drop table Orders')

# for i in range(5):
#     id = int(input("Enter Customer Id : "))
#     name = input("Enter Customer Name : ")
#     address = input("Enter Customer Address : ")
#     cur.execute(f"insert into Customer values({id},'{name}','{address}')")

# for i in range(5):
#     id = int(input("Enter Product Id : "))
#     name = input("Enter Product Name : ")
#     price = float(input("Enter Product Price : "))
#     cur.execute(f"insert into Product values({id},'{name}','{price}')")

# for i in range(11):
#     orderNo = int(input("Enter Order No : "))
#     custid = int(input("Enter Customer id : "))
#     prodNo = int(input("Enter Product Number : "))
#     qty = int(input("Enter Qty : "))
#     cur.execute(f"insert into Orders values({orderNo},{custid},{prodNo},{qty})")

# rows  = cur.execute('select * from Customer')
# rows  = cur.execute('select * from Product')
# rows  = cur.execute('select * from Orders')

# rows  = cur.execute('select * from Customer where Address = "Delhi"')   # 1)
# rows  = cur.execute('select * from Product where Price > 20 ')   # 2)
# rows  = cur.execute('select Cname from Customer where Address in ("Delhi","Chennai") ')   # 3)
# rows  = cur.execute('select OrderNo,ProdNo from Orders where Qty > 1 ')   # 4)
# rows  = cur.execute('select distinct(Cname) from Customer C,Orders O where C.Custid = O.Custid and O.OrderNo = 10005')   # 5)
# rows  = cur.execute('select P.Pname,O.Qty from Product P,Orders O where O.OrderNo = 63017 and O.ProdNo = P.ProdNo')   # 5)
# rows  = cur.execute('select O.OrderNo from Product P,Orders O where O.ProdNo = P.ProdNo and P.Pname = "Toothpaste"')   # 5)
rows  = cur.execute('select C.Cname from Product P,Customer C,Orders O where O.ProdNo = P.ProdNo and C.Custid = O.Custid and P.Pname = "Lotion"')   # 5)

for i in rows.fetchall():
    print(i)


conn.commit()
cur.close()
conn.close()