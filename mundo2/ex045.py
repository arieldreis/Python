import random
print('\033[0;97mSuas opções:\033[m \n\033[0;94m[0]PEDRA\033[m\n\033[0;94m[1]PAPEL\033[m \n\033[0;94m[2]TESOURA\033[m')
jogador = int(input('\033[0;46mQUAL É A SUA JOGADA:\033[m'))
print('JO')
print('KEN')
print('PO!!!!')

if jogador == 0:
    computador = random.randint(0,2)
    itens = ('PEDRA' , 'PAPEL' , 'TESOURA')
    print('\033[0;32m-=\033[m'*20)
    print('\033[0;91mCOMPUTADOR JOGOU {}\033[m'.format(itens[computador]))
    print('\033[0;91mJOGADOR JOGOU {}\033[m'.format(itens[jogador]))
    print('\033[0;34m-=\033[m'*20)
    #Se necessário apague esse código.
    if jogador == computador:
        print('\033[0;43mEMPATE\033[m')
    elif jogador == 0 and computador == 2: # Pedra ganha de tesoura
        print('\033[0;93mVOCÊ GANHOU\033[m')
    else:
        print('\033[0;32mVOCÊ PERDEU!!!\033[m')
elif jogador == 1:
    computador = random.randint(0,2)
    itens = ('PEDRA' , 'PAPEL' , 'TESOURA')
    print('-='*20)
    print('\033[0;94mCOMPUTADOR JOGOU {}\033[m'.format(itens[computador]))
    print('\033[0;94mJORGADOR JOGOU {}\033[m'.format(itens[jogador]))
    print('-='*20)
    #Se necessário apague o codigo.
    if jogador == computador:
        print('\033[0;96mEMPATE\033[m')
    elif (jogador == 2 and computador == 1): #Tesoura ganha de papel
        print('\033[0;95mVOCÊ GANHOU!!!\033[m')
    else:
        print('\033[0;94mVOCÊ PERDEU!!!\033[m')
elif jogador == 2:
    computador = random.randint(0,2)
    itens = ('PEDRA' , 'PAPEL' , 'TESOURA')
    print('-='*20)
    print('\033[0;33mCOMPUTADOR JOGOU {}\033[m'.format(itens[computador]))
    print('\033[0;104mJOGADOR JOGOU {}\033[m'.format(itens[jogador]))
    print('-='*20)
    if jogador == computador:
        print('\033[0;96mEMPATE\033[m')
    elif (jogador == 1 and computador == 0): #Papel ganha de pedra
        print('\033[0;90mVOCÊ PERDEU!!!\033[m')
    else:
        print('\033[0;32mVOCÊ GANHOU!!!\033[m')
else:
    print('\033[0;35;44mO NÚMERO DIGITADO NÃO CORRESPONDE AO PROGRAMA\033[m')