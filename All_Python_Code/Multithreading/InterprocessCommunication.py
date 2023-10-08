from threading import *

class Mydata:
    def __init__(self):
        self.flag = False
        self.data = 0
        self.lock = Lock()
    
    def put(self,d):
        while self.flag != False:
            pass
        self.lock.acquire()
        self.data = d
        self.flage = True
        self.lock.release()
    
    def get(self):
        while self.flag != True:
            pass
        self.lock.acquire()
        x = self.data
        self.flage = False
        self.lock.release()
        return x

def Producer(data):
    i = 1
    while True:
        data.put(i)
        print("Producer : ",i)
        i += 1

def Consumer(data):
    while True:
        x = data.get()
        print("Consumer : ",x)

data = Mydata()

t1 = Thread(target=lambda:Producer(data))
t2 = Thread(target=lambda:Consumer(data))

t1.start()
t2.start()

t1.join()
t2.join()