num = int(input('Digite um número para ver sua tabuada: '))
print('A tabuada de : {} é:'.format(num))
for n in range(1, 11):
    print('{} x {:2} = {}'.format(num, n, num*n))
