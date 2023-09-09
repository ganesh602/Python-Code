def diffBtw2Numbers(n1,n2):
    if abs(n1 - n2) <= 5:
        return True
    else:
        return False

if __name__ == '__main__':
    n1 = int(input("Enter 1st Number : "))
    n2 = int(input("Enter 2st Number : "))

    print(diffBtw2Numbers(n1,n2))
