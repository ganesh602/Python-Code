class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def show_Details(self):
        print(self.title)
        print("Book Name : ",self.title)
        print("Author Name : ",self.author)
        print("Price : ",self.price)

MyBookObj1 = Book("Freedom From the Known","Jennilia",250)
MyBookObj2 = Book("Python Crash Course","Mathew",1000)

MyBookObj1.show_Details()
print('')
MyBookObj2.show_Details()
