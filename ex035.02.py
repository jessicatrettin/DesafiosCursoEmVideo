print('-=-'*8)
print('Analisador de triângulos')
print('-=-'*8)
f1 = float(input('Primeira reta: '))
f2 = float(input('Segunda reta: '))
f3 = float(input('Terceira reta: '))
if f1 < f2 + f3 and f2 < f1 + f3 and f3 < f1 + f2:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
