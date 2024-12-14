numero_diferente = 0
tot = 0
cont = 0
numero_diferente = int(input('Digite um número [999 para parar]: '))
while numero_diferente != 999:
    tot+=numero_diferente
    cont+=1
    numero_diferente = int(input('Digite um número [999 para parar]: '))
print(f'A soma entre todos os valores equivale {tot}')
print(f"Você digitou {cont} números")
print('Fim do Programa')