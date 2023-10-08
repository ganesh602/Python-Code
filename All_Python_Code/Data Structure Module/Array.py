from array import *

arr1 = array('i',[1,2,3,4,5])
print("Integer :",arr1)

str = b'abcdef'
arr2 = array('b',str)       # b - Binary Array.
print("Binary :",arr2)      # Output will be in ASCII code of str.

print("index 0 :",arr2[0])  # Index      

print("Slicing [1:3] :",arr2[1:3])  # Slicing

arr2.append(103)            # Append
print("Append :",arr2)

print("Index of 102 :",arr2.index(102))     # Gives the index of that value.

print("Data Type :",arr2.typecode)      # Give the data type.