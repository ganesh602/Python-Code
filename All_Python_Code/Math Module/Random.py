import random

print('Random random')
print(random.random())
print(random.random())

print(random.random())

print('')
print('Random Uniform : 1-10')
print(random.uniform(1,10))
print(random.uniform(1,10))
print(random.uniform(1,10))

print('')
print('Random Uniform : 10-100')
print(random.uniform(10,100))
print(random.uniform(10,100))
print(random.uniform(10,100))
print(random.uniform(10,100))

print('')
print('Random randint : 10-100')
print(random.randint(10,100))
print(random.randint(10,100))
print(random.randint(10,100))
print(random.randint(10,100))

print('')
print('Random randrange : 10-100')  # Here we can give "Step".
print(random.randrange(10,100,5))   # And with that Step range we will get value.
print(random.randrange(10,100,5))
print(random.randrange(10,100,5))
print(random.randrange(10,100,5))

print('')
print('Random seed : 10')
random.seed(10)
print(random.random())
print(random.random())
print(random.random())

print('')
print('Again Setting Random seed : 10')
random.seed(10)
print(random.random())
print(random.random())

print('')
print('Choice : [1,2,3,4,5,6,7,8,9,10]')
L = [1,2,3,4,5,6,7,8,9,10]
print(random.choice(L))
print(random.choice(L))
print(random.choice(L))

print('')
print('Choices : [1,2,3,4,5,6,7,8,9,10]')
L = [1,2,3,4,5,6,7,8,9,10]
print(random.choices(L,k = 2))      # Here, k is choices, we can give any number of random we want.
print(random.choices(L,k = 5))
print(random.choices(L,k = 20))

print('')
print('Shuffle : [1,2,3,4,5,6,7,8,9,10]')
L = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(L)
print(L)
random.shuffle(L)
print(L)
random.shuffle(L)
print(L)

print('')
print('Random getstate')
st = random.getstate()      # Store the Current State in st.
print(random.random())
print(random.random())
print(random.random())

print('')
print('Random setstate')
random.setstate(st)         # Use that stored state to get those random numbers.
print(random.random())
print(random.random())

print('')
print('Random getrandbits of 3 i.e 2**3 = 8 , That means , it will generate under 0 to 7.')
print(random.getrandbits(3))
print(random.getrandbits(3))
print(random.getrandbits(3))