import random
import time
computador = random.randint(0,5) #faz o computador pensar
print('-=-' * 12)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 12)
print('Processando...')
time.sleep(2)
jogador = int(input('Qual número eu pensei? '))
if computador == jogador:
    print('Você venceu!')
else:
    print('Você perdeu! Eu pensei no número {}.'.format(computador))
