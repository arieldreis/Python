#radar eletrônico
velocidade = int(input('Qual é a velocidade atual do seu carro: ')) #Pede ao usuário solicitar a velocidade do seu carro. 
a = 80
if velocidade <= a: #condição onde mostra que a velocidade do carro está abaixo de 80km/h
    print('Tenha um bom dia! Dirija com segurança.')
else:
    multa = (velocidade-80) * 7 + 53.20 #calculo para a decisão da multa
    print('Você está a velocidade de {} km/h e o limite é {} km/h \n Você será multado no valor de R${}'.format(velocidade, a, multa))