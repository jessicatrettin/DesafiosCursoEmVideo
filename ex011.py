b = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
A = b * h
t = A / 2
print('A dimensão da sua parede é {}x{}m e a área {:.2f}m².'.format(b, h, A))
print('São necessários {:.2f}l de tinta para pintar sua parede.'.format(t))
