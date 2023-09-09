def SumOfScoresEndingWithZeroes(Scores):
    sum = 0
    for i in Scores:
        if i % 10 == 0:
            sum += i
    return sum

if __name__ == "__main__":
    Scores = [int(x) for x in input("Enter Numbers : ").split()]
    #Scores = [200,456,300,100,234,678]
    sum = SumOfScoresEndingWithZeroes(Scores)
    print("Sum of the Numbers is ",sum)