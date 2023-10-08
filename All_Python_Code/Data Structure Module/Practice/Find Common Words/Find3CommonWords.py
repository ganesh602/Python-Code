from collections import Counter
import re

file = open("D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\Data Structure Module\Practice\Find Common Words\FindCommonWords.txt",'r')
str = file.read()

lst = [x for x in str.split()]      # This will also work.
str = re.findall('\w+',str)         # This will also work. This is most efficient.

c = Counter(str).most_common(3)

print(c)