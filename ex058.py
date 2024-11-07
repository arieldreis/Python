'''import random
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
print('Você acertou, porém voc precisou de {} tentativas!'.format(palpites))'''
import random
mensagem = "NÚMERO MALUCO!!!"
largura_total = 80
print('\033[0;36m=-=\033[m'*30)
print(f'\033[0;36m{mensagem.center(largura_total)}\033[m')
print('\033[0;36m=-=\033[m'*30)
jogador = 0
tentativa = 0
total = 0
computador = (random.randint(1, 100))
while jogador != computador and tentativa != computador:
    jogador = int(input('Tente adivinhar um número que eu estou pensando: '))
    if jogador < computador:
        print('Você jogou o número {} e o número que a máquina pensou é maior!'.format(jogador))
    elif jogador > computador:
        print('Você jogou o número {} e o número que o computador pensou é menor!'.format(jogador))
    total+=1
print('Parabéns você ganhou e precisou de {} tentativas'.format(total))
print(f'O número que eu escolhi foi {computador}')