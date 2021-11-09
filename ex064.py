n = q = s = n2 = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    q += 1
    n2 += n
    s = n2 + n
q -= 1
s -= 1998
print('Você digitou {} números, a soma entre eles dá {}.'.format(q,s))
