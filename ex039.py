from datetime import date
hoje = date.today()
print('Qual o seu sexo? ')
print('\033[31m*\033[m'*25)
print('[ 1 ] Feminino \n[ 2 ] Masculino')
print('\033[31m*\033[m'*25)
sexo = int(input('Opção: '))
if sexo == 1:
    print('Obrigado! Você não precisa se alistar.')
elif sexo == 2:
    nasc = int(input('Em que ano você nasceu? '))
    idade = hoje.year - nasc
    if idade < 18:
        falta = 18 - idade
        print('''De acordo com a sua idade, você ainda vai se alistar para o serviço militar.
Faltam {} anos para isso acontecer.'''.format(falta))
    elif idade == 18:
        print('De acordo com sua idade, esse ano você deve se alistar ao serviço militar.')
    else:
        passou = idade - 18
        print('De acordo com a sua idade, já se passaram {} do seu alistamento ao exército.'.format(passou))
else:
    print('OPÇÃO INVÁLIDA!')