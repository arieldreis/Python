import random
import emoji
msg = "VAMOS JOGAR PAR OU ÍMPAR"
print("=-"*40)
print(msg.center(80))
print("=-"*40)
cont = 0
while True:
    computador = int(random.randint(0, 10))
    parimp = int(input("Digite um valor: "))
    escolha: str = str(input("Par ou Ímpar? [P/I]: ")).upper()
    if parimp < 0 or parimp > 10:
        print("FIM DO PROGRAMA!")
        break
    soma = parimp + computador
    if soma % 2 == 0 and escolha == "P":
            print("=-"*30)
            print(f"Você jogou {parimp} e o computador {computador}")
            print(f"Total de {soma} DEU PAR")
            print("VOCÊ GANHOU \U0001F604 \U0001F389 \U0001F3C6 \U0001F680 \U00002B50")
            print("=-"*30)
            break
    elif soma % 2 != 0 and escolha == "I":
        print("=-" * 30)
        print(f"Você jogou {parimp} e o computador {computador}")
        print(f"Total de {soma} DEU IMPAR")
        print('VOCÊ GANHOU! \U0001F604 \U0001F389 \U0001F3C6 \U0001F680 \U00002B50')
        print("=-" * 30)
        break
    else:
        print("=-"*30)
        print("VOCÊ PERDEU!!\U0001F641 \U0001F622 \u274C")
        print("JOGUE NOVAMENTE!!")
        print("=-" * 30)
    cont+=1
print(f"Você precisou de {cont} vezes parar ganhar o jogo.")