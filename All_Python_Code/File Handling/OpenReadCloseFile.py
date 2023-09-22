file = open(r'D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\test.txt','r')
# The r prefix ensures that the string file_path is treated as a raw string, 
# allowing you to specify the file path exactly as it appears, with backslashes being treated as literal characters. 
# This is commonly used when working with file paths in Windows.
str = file.read(6)
print(str)
str = file.read()
print(str)

