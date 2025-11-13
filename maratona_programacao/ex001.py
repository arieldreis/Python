# Exemplo C
import math
print("Seja bem-vindo ao nosso programa!")
while True:
    quantidade = int(input())
    if quantidade == 0:
        break
    total_KM = 0
    total_Litros = 0
    melhor_consumo = 0.0

    for i in range(quantidade):
        litros_abastecidos, quilômetros_rodados = map(int, input().split())
        total_KM += quilômetros_rodados
        total_Litros += litros_abastecidos

        if litros_abastecidos != 0:
            consumo_individual = quilômetros_rodados / litros_abastecidos
            if consumo_individual > melhor_consumo:
                melhor_consumo = consumo_individual
    if total_Litros != 0:
        consumo_medio_geral = total_KM / total_Litros
    else:
        consumo_medio_geral = 0
    truncado = math.trunc(consumo_medio_geral * 10) / 10
    truncado_melhor = math.trunc(melhor_consumo * 10) / 10
    print(f"Consumo médio geral: {truncado:.1f}")
    print(f"Melhor consumo individual: {truncado_melhor:.1f}")