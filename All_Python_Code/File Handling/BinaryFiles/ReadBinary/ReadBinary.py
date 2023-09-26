with open("D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\BinaryFiles\ReadBinary\my.data","rb") as file:
    #str = file.read(5)      # O/P :-  b'abcde'  - b is showing for binary.
    str = file.read(5).decode()   # O/P: :-  abcde  - this will remove 'b'.
    print(str)
    file.seek(-3,1)     # Setting the file Pointer as 'c'.
    print(file.read(1).decode())    # Now file Pointer is at 'c', onlly reading 'c' character.
    print(file.tell())      # tell - it will show where the file pointer is currently at which index.