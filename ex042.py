print('\033[31m-=-\033[m' * 8)
print('Analisador de triângulos')
print('\033[31m-=-\033[m' * 8)
l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('É possível formar um triângulo.')
    if l1 == l2 == l3:
        print('Todos os lados do seu triângulo são iguais. Portanto, seu triângulo é EQUILÁTERO.')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('Dois lados do seu triângulo são iguais e um é diferente. Portanto, seu triângulo é ISÓSCELES.')
    elif l1 != l2 != l3 != l1:
        print('Todos os lados do seu triângulo são diferentes. Portanto, seu triângulo é ESCALENO.')
else:
    print('Não é possível formar um triângulo com os valores informados.')
