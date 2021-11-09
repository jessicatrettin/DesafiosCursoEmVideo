frase = str(input('Digite uma frase: ')).upper()
junto = frase.replace(' ', '')
n = len(junto)
inverso = junto[::-1]
if inverso == junto:
    print('A frase {} é um palíndromo.'.format(frase))
else:
    print('A frase {} não é um palíndromo.'.format(frase))