# INR = 83.11 USD
class Currency:
    def __init__(self,currency_name,rate):
        self.currency_name = currency_name
        self.rate = rate

    def get_rate(self):
        return self.rate
    
    def get_currency(self):
        return self.currency_name

    def set_rate(self,rate):
        self.rate = rate
    
    def set_currency(self,currency_name):
        self.currency_name = currency_name

    def convert(self,amount):
        return self.currency_name + " conversion is " + str(self.rate * amount)
    
c = Currency('USD',70)
print(c.convert(100))

c.set_currency('AUD')
c.set_rate(50)
print(c.convert(100))
