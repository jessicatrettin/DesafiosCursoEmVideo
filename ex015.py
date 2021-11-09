dia = int(input('Por quantos dias o carro foi alugado? '))
km = int(input('Quantos km rodados? '))
tap = (60 * dia) + (0.15 * km)
print('O total à pagar pelo aluguel do carro é R$ {:.2f}.'.format(tap))
