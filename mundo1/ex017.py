import math
oposto = float(input("Qual é o comprimento do cateto oposto: "))
adjacente = float(input("Qual é o comprimento do cateto adjacente: "))
hispotenusa = math.hypot(oposto,adjacente)
print(f"Com os valores do cateto de {oposto} e {adjacente} é igual á {hispotenusa:.2f}")