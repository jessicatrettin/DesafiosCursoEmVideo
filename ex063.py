print('-'*45)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*45)
qtd = int(input('Digite quantos termos você quer mostrar: '))
term = 0
p = 0
s = 1
qt = 3
print('~'*45)
if qtd == 0:
    print('Nenhum termo à ser mostrado!')
if qtd == 1:
    print ('{} - '.format(p), end='')
if qtd == 2:
    print ('{} - {} - '.format(p,s), end='')
else:
    print('{} - {} - '.format(p, s), end='')
    while qt <= qtd:
        t = p + s
        print('{} - '.format(t), end='')
        p = s
        s = t
        qt += 1
print('FIM')
