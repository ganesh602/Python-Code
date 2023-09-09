def pangram(phrase):
    str = 'abcdefghijklmnopqrstuvwxyz'
    str = set(str)
    phr = set(phrase)

    # return phr >= str
    #---OR
    # if phr >= str:            #Checks if phr is superset or greater than str.
    #     return True
    # else:
    #     return False
    ##########---OR----############
    for i in str:
        if i not in phrase:
            return False
    return True

strin = 'The quick brown fox jumps over the lazy dog'
strin = strin.lower()
print(pangram(strin))