import random
print('Vamos jogar um jogo eu irei pensar um número de 0 á 100 tente adivinhar, pode ser? ')
computador = (random.randint(0, 10))
acertou = False
palpites = 0
while  not acertou:
    jogador = int(input('Digite um número de 0 á 100 por favor:'))
    if jogador == computador:
        palpites+=1
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez')
        else:
            print('Menos... tente mais uma vez.')
print('Você acertou, porém voc precisou de {} tentativas!'.format(palpites))