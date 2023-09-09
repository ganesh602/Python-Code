def MaxBtw3Numbers(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

if __name__ == "__main__":
    n1 = int(input("Enter 1st Number : "))
    n2 = int(input("Enter 2nd Number : "))
    n3 = int(input("Enter 3rd Number : "))

    print(MaxBtw3Numbers(n1,n2,n3))