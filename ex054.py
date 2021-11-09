from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for n in range(1,8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(n)))
    if (ano - nasc) >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('{} pessoas são maiores de idade e {} são menores.'.format(totmaior, totmenor))
