n = int(input('Qual o primeiro termo? '))
p = int(input('Qual a razão da progressão? '))
t = 0
prog = n
print('{} - '.format(n), end='')
while t < 9:
    prog = prog + p
    t += 1
    print('{} - '.format(prog), end='')
print('FIM')