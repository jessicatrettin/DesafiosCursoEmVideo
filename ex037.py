num = int(input('Digite um número inteiro: '))
print('\033[1m-=-\033[m'*15)
print('Você quer que o número seja convertido para:')
print('''\033[34m[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL\033[m''')
print('\033[1m-=-\033[m'*15)
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mERRO! Tente novamente.')
