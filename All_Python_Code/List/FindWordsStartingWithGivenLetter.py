food = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
letter = input('Enter a letter : ')

found = False
for i in food:
    if i.startswith(letter):
        found = True
        print('Word : ', i)
if found is False:
    print('No word Start with that Letter.')
