# Um exercício da fundação Bradesco
def lerNota(n1, n2):
    media = (n1 + n2) / 2
    if media >= 7.0:
        print("Aprovado!")
    else:
        print("Reprovado!")
# Entrada de dados
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
# Entrada dos paramêtros da função
lerNota(nota1, nota2)
