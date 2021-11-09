casa = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você vai pagar? '))
prest = casa / (anos * 12)
if prest > (salario * 30 / 100):
    print('''Empréstimo \033[31mnegado\033[m!
A prestação do empréstimo fica R$ {:.2f}.
Esse valor é superior à 30% do seu salário.'''.format(prest))
else:
    print('''Empréstimo \033[32maprovado\033[m!
A prestação do empréstimo fica R$ {:.2f}.'''.format(prest))
