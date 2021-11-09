preço = float(input('Qual o valor do produto? R$ '))
print('-'*30)
print('''Condições de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
print('-'*30)
cond = int(input('Qual a condição de pagamento escolhida? '))
if cond == 1:
    novo = preço * 0.9
    print('Valor à ser pago R$ {:.2f}.'.format(novo))
elif cond == 2:
    novo = preço * 0.95
    print('Valor à ser pago R$ {:.2f}.'.format(novo))
elif cond == 3:
    parc = preço / 2
    print('Você pagará R$ {:.2f} em 2x de R$ {:.2f}.'.format(preço, parc))
elif cond == 4:
    qtd = int(input('Quantas parcelas? '))
    novo = preço * 1.2
    parc = novo / qtd
    print('Você pagará R$ {:.2f} em {}x de R$ {:.2f}.'.format(novo, qtd, parc))
else:
    print('\033[31mOpção inválida! Tente novamente.\033[m')
