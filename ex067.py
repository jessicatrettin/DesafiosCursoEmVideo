n = 0
while n >= 0:
    n = int(input('Digite um número do qual você quer ver a tabuada: '))
    multiplicador = 0
    while multiplicador <= 9:
        multiplicador += 1
        print('{} x {} = {}'.format(n, multiplicador, n * multiplicador))
print('Módulo de tabuada encerrado!')
