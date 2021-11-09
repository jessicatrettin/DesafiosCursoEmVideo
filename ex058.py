import random
import time
computador = random.randint(0,10) #faz o computador pensar
print('-=-' * 12)
print('Vou pensar em um número de 0 a 10. \nTente adivinhar...')
print('-=-' * 12)
print('Processando...')
time.sleep(2)
jogador = int(input('Qual número eu pensei? '))
tentativas = 1
while computador != jogador:
    tentativas += 1
    if jogador < computador:
        jogador = int(input('Mais... Tente novamente: '))
    else:
        jogador = int(input('Menos... Tente novamente: '))
print('Você VENCEU!')
print('Foram feitas {} tentativas.'.format(tentativas))