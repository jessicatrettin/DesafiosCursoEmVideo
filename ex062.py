n = int(input('Qual o primeiro termo? '))
p = int(input('Qual a razão da progressão? '))
t = 1
prog = n
print('{} - '.format(n), end='')
total = 0
resp = 10
while resp != 0:
    total = total + resp
    while t <= total:
        print('{} - '.format(prog), end='')
        prog += p
        t += 1
    print('PAUSA')
    resp = int(input('Quantos termos a mais você quer mostrar? '))
print('AO todo, foram mostrados {} termos da PA.'.format(total))
print('FIM')