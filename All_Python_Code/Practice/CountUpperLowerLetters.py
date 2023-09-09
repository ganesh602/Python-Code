def countLetters(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():
            upper += 1
        elif  i.islower():
            lower += 1
    return lower,upper

str = "AbcDEfgh"
lower,upper = countLetters(str)
print("Lower Letters : ",lower)
print("Upper Letters : ",upper)