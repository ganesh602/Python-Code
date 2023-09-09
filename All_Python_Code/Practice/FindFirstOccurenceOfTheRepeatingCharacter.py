# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    S = input()
    #S = input("Enter Number OF String : ")

flag = False
for i in range(len(S)-1):
    if S[i].isalnum() == True:
        if S[i] == S[i+1]:
            flag = True
            print(S[i])
            break
        
if flag == False:
    print(-1)