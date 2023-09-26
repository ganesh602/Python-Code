file = open("D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\CopyingBinaryFiles\python1.png",'rb')
data = file.read()

copyfile = open("D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\CopyingBinaryFiles\python2.png",'wb')
copyfile.write(data)    # Reading file data and storing in the copyfile to make a copy. 

file.close()
copyfile.close()
            