qtd = 0
s = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        qtd += 1 # qtd = qtd + 1
        s += n # s = s + n
print('O somatório de todos os {} números múltiplos de 3, no intervalo de 1 até 500 é {}'.format(qtd, s))
