n = contador = soma = 0
while n != 999:
    n = int(input('Digite um número inteiro (999 para parar): '))
    contador += 1
    soma += n
print('Foram digitados {} números até a parada.'.format(contador))
print('A soma entre os números digitados é de {}.'.format(soma))