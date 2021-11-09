v = float(input('Qual a velocidade em km/h? '))
if v > 80:
    print('Você excedeu o limite de velocidade e foi multado!')
    print('Sua multa foi de R$ {:.2f}.'.format((v-80)*7))
print('Tenha um bom dia! Dirija com segurança.')