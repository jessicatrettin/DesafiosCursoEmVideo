n = int(input('Digite um número para ver seu fatorial: '))
mult = n
fatorial = 1
print('Calculando {}! = '.format(n), end='')
while mult > 0:
    print('{}'.format(mult),end='')
    print(' x ' if mult > 1 else ' = ', end='')
    fatorial *= mult
    mult -= 1
print('{}.'.format(fatorial), end='')
