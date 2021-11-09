print('='*30)
print('{:^30}'.format('PROGRESSÃO ARITMÉTICA'))
print('='*30)
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for prog in range(pt, (pt+(10*r)), r):
    print(prog, end=' > ')
print('ACABOU')