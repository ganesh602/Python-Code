#----Normal Function-------
# def milesToKm(miles):
#     return 1.6 * miles
# print(milesToKm(10))

# ---Lambda Function For Converting Miles To Km ---
k = lambda miles: 1.6 * miles
print(k(10))

# ---Lambda Function For Adding Numbers ---
k = lambda x,y: x + y 
print(k(10,12))

# ---Lambda Function For Printing Greater Number ---
k = lambda x,y,z: max(x,y,z) 
print(k(10,12,5))
# -- with Logic------
k1 = lambda x,y,z: x if (x > y and x > z) else (y if y > z else z) 
print(k1(10,50,5))

ans=input("the capital of canada is :")
if(ans=="ottawa"):
    print("you are wise")
else:
    print("you are ignorant")