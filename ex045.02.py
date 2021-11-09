from random import randint
from time import sleep
lista = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('{:*^40}'.format(' PEDRA, PAPEL, TESOURA! '))
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
op = int(input('Sua opção: '))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
sleep(1)
print('*'*30)
print('O computador escolheu {}'.format(lista[comp]))
print('Você escolheu {}'.format(lista[op]))
print('*'*30)
if op == 0:
    if comp == 0:
        print('Empate!')
    elif comp == 1:
        print('Ganhei!')
    elif comp == 2:
        print('Você ganhou!')
elif op == 1:
    if comp == 0:
        print('Você ganhou!')
    elif comp == 1:
        print('Empate!')
    elif comp == 2:
        print('Ganhei!')
elif op == 2:
    if comp == 0:
        print('Ganhei!')
    elif comp == 1:
        print('Você ganhou!')
    elif comp == 2:
        print('Empate!')
else:
    print ('Opção inválida! Tente novamente!')