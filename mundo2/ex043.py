#Calculo de IMC
massa = float(input('Qual é a sua massa corporal: '))
altura = float(input('Qual é a sua altura: '))
calculo = massa/(altura**2)
if calculo < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= calculo < 25:
    print('Peso normal.')
elif 25 <= calculo < 30:
    print('Sobrepeso')
elif 30 <= calculo < 40:
    print('Obesidade')
else:
    print('Obesidade morbita!!!!!!')