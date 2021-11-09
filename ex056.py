med = 0
idadehomem = 0
homemvelho = ''
mulher = 0
for n in range(1,5):
    print('----- {}ª PESSOA -----'.format(n))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [ F | M ]: '))
    med += idade
    if n == 1 and sexo in 'Mm':
        idadehomem = idade
        homemvelho = nome
    if sexo in 'Mm' and idadehomem < idade:
        idadehomem = idade
        homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1
media = med / 4
print('A média de idade de todas as pessoas é {} anos.'.format(media))
print('O homem mais velho é {} com {} anos.'.format(homemvelho, idadehomem))
print('O grupo possui {} mulheres com menos de 20 anos.'.format(mulher))