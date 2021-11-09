frase = str(input('Digite uma frase: ')).upper().strip()
print('Na frase {} a letra A aparece {} vezes.'.format(frase, frase.count('A')))
print('Na frase {} a letra A aparece pela primeira vez na posição {}.'.format(frase, frase.find('A')))
print('Na frase {} a letra A aparece pela última vez na porição {}.'.format(frase, frase.rfind('A')))
