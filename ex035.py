print('-=-'*8)
print('Analisador de triângulos')
print('-=-'*8)
f1 = float(input('Primeira reta: '))
f2 = float(input('Segunda reta: '))
f3 = float(input('Terceira reta: '))
maior = f1
if f2 > f1 and f2 > f3:
    maior = f2
if f3 > f1 and f3 > f2:
    maior = f3
if f1 + f2 + f3 - maior > maior:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')
