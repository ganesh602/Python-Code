def decorator(myfunc):
    def wrapper(msg):
        print("*" * 10)
        myfunc(msg)
        print("*" * 10)
    return wrapper

@decorator
def myfunc(msg):
    print(msg)

#d = decorator(myfunc)
myfunc('Ganesh')

#       OR

# def decorator(myfunc):
#     def wrapper():
#         print("*" * 10)
#         myfunc()
#         print("*" * 10)
#     return wrapper

# def myfunc():
#     print("This is an Example of Decorator.")

# d = decorator(myfunc)
# d()