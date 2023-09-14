class Customer:
    def __init__(self,id,name,bDoorNo,bStreet,bCity,bCountry,bPin,SDoorNo,SStreet,SCity,SCountry,SPin):
        self.ID = id
        self.Name = name
        self.BillingAddress = self.Address(bDoorNo,bStreet,bCity,bCountry,bPin)
        self.ShippingAddress = self.Address(SDoorNo,SStreet,SCity,SCountry,SPin)

    class Address:
        def __init__(self,DoorNo,Street,City,Country,Pin):
            self.DoorNo = DoorNo
            self.Street = Street
            self.City = City
            self.Country = Country
            self.Pin = Pin
        
        def DisplayBilling(self):
            print(self.DoorNo)
            print(self.Street)
            print(self.City)
            print(self.Country)
            print(self.Pin)

c = Customer(1,'John',101,'Vashi','Mumbai','India',400070,101,'VashiNaka','Mumbai','India',400074)
c.BillingAddress.DisplayBilling()
c.ShippingAddress.DisplayBilling()
