with open("D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\BinaryFiles\ReadBinary\my.data","wb") as file:
    file.write(b"abcdefghij")        # b - for binary
    # file.write("abcdefghi".encode())   # encode - converts to binary
