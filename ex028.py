import random

apresentacao = input('Vamos jogar um jogo eu irei pensar um número de 0 á 100 tente adivinhar, pode ser? ')
numero_pensar = int(input('Digite um número de 0 á 100 por favor:'))
computador = (random.randint(0, 100))

if numero_pensar == computador:
     print('Você acertou, meus parabéns!')
else:
    print('Eu pensei no número {} e não no {}'.format(computador, numero_pensar))