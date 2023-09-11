def div(a,b):
    try:
        c = a // b
        return c
    except ZeroDivisionError as err:
        raise ZeroDivisionError
    finally:
        print("Function Executed")
c = div(200,0)
print(c)
