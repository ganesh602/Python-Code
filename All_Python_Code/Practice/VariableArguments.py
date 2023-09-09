def minimum(*var,lowLimit = None):
    var = list(var)
    if lowLimit is None:
        return min(var)
    else:
        min2 = [x for x in var if x >= lowLimit]
        return min(min2)
    
min1 = minimum(1,5,2,-5,10,12,20,-10,25)
min2 = minimum(1,5,2,-5,10,12,20,-10,25,lowLimit=11)

print(min1 ,"and ", min2)

