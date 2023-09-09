import random

attempt = 1
rand = random.randint(1, 10)
guess = int(input('Guess the Number Between 1 to 10 : '))

while guess != rand:
    if guess > rand:
        guess = int(input('Enter Smaller Number :'))
    elif guess < rand:
        guess = int(input('Enter Greater Number :'))
    attempt += 1

if guess == rand:
    print(f'You Guessed Right at {attempt} attempts!')
