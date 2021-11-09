dist = float(input('Qual a distância da sua viagem? '))
if dist <= 200:
    p = dist * 0.50
else:
    p = dist * 0.45
print('O preço da passagem é R$ {:.2f}.'.format(p))
