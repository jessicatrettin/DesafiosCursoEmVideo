from datetime import date
ano = date.today().year
nasc = int(input('Ano de nascimento? '))
idade = ano - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('A categoria é MIRIM.')
elif idade <= 14:
    print('A categoria é INFANTIL.')
elif idade <= 19:
    print('A categoria é JÚNIOR.')
elif idade <= 25:
    print('A categoria é SÊNIOR')
elif idade > 25:
    print('A categoria é MASTER.')
