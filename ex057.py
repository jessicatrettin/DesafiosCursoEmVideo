sexo = str(input('Informe seu sexo [ F | M ]: ')).strip().upper()[0]
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados incorretos. Digite seu sexo novamente: ')).strip().upper()[0]
if sexo == 'F':
    print('Sexo feminino registrado corretamente.')
else:
    print('Sexo masculino registrado corretamente.')