from ClsStudent import *
from pickle import *

stud = [Student(1,'ganesh','IT'),Student(2,'john','CS'),Student(3,'rohan','BAF')]

with open("D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\PickleAndUnpickle\Students.data",'wb') as file:
    for s in stud:
        dump(s,file)

