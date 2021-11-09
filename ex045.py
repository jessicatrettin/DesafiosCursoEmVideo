import random
print('{:*^40}'.format(' PEDRA, PAPEL, TESOURA! '))
print('''[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
op = int(input('Sua opção: '))
ppt = [1, 2, 3]
comp = random.choice(ppt)
print('Minha opção: {}'.format(comp))
if op == comp:
    print('Empate!')
elif op == 1 and comp == 2:
    print('Ganhei!')
elif op == 1 and comp == 3:
    print('Você ganhou!')
elif op == 2 and comp == 1:
    print('Você ganhou!')
elif op == 2 and comp == 3:
    print('Ganhei!')
elif op == 3 and comp == 1:
    print('Ganhei!')
elif op == 3 and comp == 2:
    print('Você ganhou!')
else:
    print('\033[31mOpção inválida, tente novamente!')