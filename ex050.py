nn = 0
qtd = 0
for n in range(1, 7):
    n = float(input('Digite o {}° número: '.format(n)))
    if n % 2 == 0:
        nn += n
        qtd += 1
print('A soma dos {} números pares é: {}'.format(qtd, nn))
