sal = float(input('Qual o seu salário? R$ '))
if sal > 1250.00:
    aum = sal * 10 / 100
else:
    aum = sal * 15 / 100
novo = sal + aum
print('O seu aumento é de R$ {:.2f}, você passa a ganhar R$ {:.2f}.'.format(aum, novo))
