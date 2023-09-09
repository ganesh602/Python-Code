def message(name,profession,/):
    if profession[0] in 'aeiouAEIOU':
        print(f'My name is {name}, I am an {profession}')
    else:    
        print(f'My name is {name}, I am a {profession}')

if __name__ == "__main__":
    name = input("Enter Your Name : ")
    profession = input("Enter Your Profession : ")

    message(name,profession)