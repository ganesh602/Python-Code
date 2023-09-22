class Customer:
    def __init__(self,name,phone_no):
        self.name = name
        self.phone_no = phone_no

    def get_Name(self):
        return self.name

    def get_PhoneNo(self):
        return self.phone_no
    
    def set_PhoneNo(self,PhoneNo):
        self.phone_no = PhoneNo

cust = Customer("Ganesh",122)
print("Name : ",cust.get_Name())
print("Phone No. : ",cust.get_PhoneNo())

cust.set_PhoneNo(8369)
print("Phone No. : ",cust.get_PhoneNo())



    