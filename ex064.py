numero_diferente = 0
tot = 1
while numero_diferente != 999:
    numero_diferente = int(input('Digite um número [999 para parar]: '))
    tot+=numero_diferente
print(f'A soma entre todos os valores é igual á {tot}')
print('Fim do Programa')