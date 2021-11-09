resposta = 0
operação = 0
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print('='*25)
print('''O que você deseja fazer:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
print('='*25)
resposta = int(input('Sua opção: '))
while resposta != 5:
    if resposta == 1:
        operação = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, operação))
        resposta = int(input('Sua opção: '))
    if resposta == 2:
        operação = n1 * n2
        print('A multiplicação entre {} e  {} é {}.'.format(n1, n2, operação))
        resposta = int(input('Sua opção: '))
    if resposta == 3:
        if n1 > n2:
            operação = n1
            print('O número {} é maior que {}.'.format(n1, n2))
        if n2 > n1:
            print('O número {} é maior que {}.'.format(n2, n1))
        resposta = int(input('Sua opção: '))
    if resposta == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        resposta = int(input('O que você deseja fazer agora? '))
print('FIM')