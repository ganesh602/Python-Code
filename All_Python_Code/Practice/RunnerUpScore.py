if __name__ == '__main__':
    n = int(input("Enter number : "))
    arr = map(int, input().split())

    lst = list(arr)

    sortlst = sorted(lst, reverse=True)

    last = 0
    for i in range(1, len(sortlst)):
        if sortlst[i] < sortlst[0]:
            last = i
            break

    # print(sorted_arr[len(sorted_arr) - 3])
    print(sortlst[last])
