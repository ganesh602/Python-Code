import ClsStudent,pickle
with open("D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\PickleAndUnpickle\Students.data","rb") as file:
    for i in range(3):
        StudentObj = pickle.load(file)
        StudentObj.display()
        print('')
