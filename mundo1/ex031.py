#custo da viagem
distancia = int(input('Qual é a distância da sua viagem? '))
if distancia <= 200:
    calculo1 = (distancia * 0.50) + distancia
    print('O valor da sua viagem ficará no valor de R${:.2f}'.format(calculo1))
elif distancia > 200:
    calculo2 = (distancia * 0.45) + distancia
    print('O valor da sua viagem ficará no valor R${:.2f}'.format(calculo2))