peso = float(input('Digite o seu peso em quilos: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura * altura)
print('Para o peso {:.2f}kg e altura de {:.2f}m, seu IMC é {:.1f}: '.format(peso, altura, imc), end='')
if imc < 18.5:
    print('\033[31mABAIXO DO PESO\033[m')
elif 18.5 <= imc < 25:
    print('\033[32mPESO IDEAL\033[m')
elif 25 <= imc < 30:
    print('\033[33SOBREPESO\033[m')
elif 30 <= imc < 40:
    print('\033[31mOBESIDADE\033[m')
elif 40 <= imc:
    print('\033[31mOBESIDADE MÓRBIDA\033[m')
