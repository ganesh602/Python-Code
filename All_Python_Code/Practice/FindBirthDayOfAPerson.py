dict1 = {'ganesh':'06062001','dhana':'27032000','raj':'15072000'}
name = input("Enter a Name : ")

# Using If Condition:
if name in dict1:
    #Any Method can work.
    print('Mr/Mrs {} was born on {}'.format(name,dict1[name]))
    #print(dict1[name])
    #print(f'Mr/Mrs {name} was born on {dict1[name]}')#.format(name,dict1[name]))
else:
    print("Name is not there.")

# # Using For Loop:
# flag = False
# for i in dict1:
#     if i == name:
#         flag = True
#         print(dict1[i])
# if flag == False:
#     print("Name is not there.")