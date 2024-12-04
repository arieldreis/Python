'''import time
cont = 1
while cont <= 11:
    print(cont)
    time.sleep(1)
    cont+=1
print('FIM!')'''

'''n = 0
soma = 0
while n < 10:
    n = int(input('Digite um número:'))
    if n < 0:
        print('Você digitou um número negativo!')
        break
    soma += n
print('A soma dos valores é igual {}'.format(soma))
print('FIM DO PROGRAMA')'''

''' import random
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
print(f'O número que eu escolhi foi {computador}') '''

'''tabuada = int(input('Digite um número:'))
tot = 10
while tabuada <= tot:
    multiplicacao = tabuada * tot
    print(f'{tabuada} x {tabuada} = {multiplicacao}')'''
'''inicio = int(input('Qual é o valor que você quer começar: '))
fim = int(input('Qual é o termo final que vc quer mostrar: '))
passo = inicio
cont = 1
while cont <= 10:
    passo = int(input('Qual é o número de passos: '))
    inicio+=passo
    cont+=fim
    print(f'{cont}' , end=' - ')'''
km = float(input('Quantos Km o automovél irá rodar: '))
tot = (km * 1.50) + 9
print('O valor a ser pago no frete será de R${:.2f}'.format(tot))