def aumento(salario):
    return salario + (salario * 0.15)
salario = float(input("Qual é o salário do funcionário: R$"))
print(f"Um funcionário que ganhava R${salario}, com 15% de aumento passa a receber R${aumento(salario):.2f}")