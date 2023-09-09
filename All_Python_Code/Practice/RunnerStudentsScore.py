if __name__ == '__main__':

    store = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp = [name, score]
        store.append(temp)


    # print(store)

    # Input list
    # sub_li = [['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]

    # Printing the list
    # print(Sort(sub_li))

    # Python code to sort the lists using the second element
    # of sublists inplace way to sort, use of third variable
    def Sort(sub_li):
        l = len(sub_li)

        for i in range(0, l):
            for j in range(0, l - i - 1):

                if (sub_li[j][1] > sub_li[j + 1][1]):
                    tempo = sub_li[j]
                    sub_li[j] = sub_li[j + 1]
                    sub_li[j + 1] = tempo
        return sub_li


    sortlst = Sort(store)
    # sortlst = sorted(store, reverse=False)

    index = 0
    for i in range(0, len(sortlst)):
        if sortlst[i][1] > sortlst[0][1]:
            index = i
            break

    lstHold = [sortlst[index][0]]
    # print(sortlst[index][0])

    for i in range(0, len(sortlst)):
        if i != index:
            if sortlst[i][1] == sortlst[index][1]:
                index = i
                lstHold.append(sortlst[index][0])
                # print(sortlst[index][0])

    s1 = sorted(lstHold, reverse=False)

    for i in s1:
        print(i)


