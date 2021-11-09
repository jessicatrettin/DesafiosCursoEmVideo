frase = str(input('Digite uma frase: ')).upper()
junto = frase.replace(' ', '')
n = len(junto)
inverso = ''
for f in range(n-1, -1, -1):
    inverso += junto[f]
if inverso == junto:
    print('A frase {} é um palíndromo.'.format(frase))
else:
    print('A frase {} não é um palíndromo.'.format(frase))
