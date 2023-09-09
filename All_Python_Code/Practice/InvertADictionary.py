# eg. Before - {'a':10,'b':20,'c':30,'d':40}
#      After - {10:'a',20:'b',30:'c',40:'d'}

def invert(dict):
    newDict = {}
    for key,value in dict.items():
        newDict[value] = key
    return newDict

dict = {'a':10,'b':20,'c':30,'d':40}

newDict = invert(dict)
print("Before : ",dict)
print("After : ",newDict)
