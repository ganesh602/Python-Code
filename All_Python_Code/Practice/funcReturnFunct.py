def outer():
    def inner():
        print("Hello World.")
    return inner

d = outer()

d()