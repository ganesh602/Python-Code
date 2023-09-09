# for i in range(0, 5):
#    for j in range(0, 5):
#        print('(', i, ',', j, ')', end=' ')
#    print('')

for i in range(0, 5):
    for j in range(0, 5):
        if i >= j:
            print('*', end=' ')
    print('')
