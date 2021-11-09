import math
num = resp = soma = quant = med = maior = menor =0
while resp != 'N':
    num = int(input('Digite um número: '))
    resp = str(input('Você quer continuar? [ S | N ]: ')).upper()
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
med = soma / quant
print('A média dos números digitados é {}.'.format(med))
print('O maior número é {} e o menor é {}.'.format(maior,menor))
