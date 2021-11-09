n = int(input('Digite um número para saber se ele é primo: '))
c = 0
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        tot += 1
        print('\033[31m', end=' ')
    else:
        print('\033[32m', end=' ')
    print('{}'.format(c), end=' ')
print('\33[m\nO número {} foi divisível {} vezes.'.format(n, tot))
if tot == 2:
    print('Portanto ele É PRIMO!')
else:
    print('Portanto ele NÃO É PRIMO!')
