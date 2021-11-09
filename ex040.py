n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Sua média é: {:.2f}'.format(media))
if media < 5:
    print('Você está \033[31mREPROVADO\033[m.')
elif 7 > media >= 5:
    print('Você está em \033[33mRECUPERAÇÃO\033[m')
elif media >= 7:
    print('Você está \033[32mAPROVADO\033[32m')
