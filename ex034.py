#Aumento de salário
salario = float(input('Digite o seu salário, por favor: '))
if salario > 1250:
    aumento = (salario*0.10) + salario
    print('O salário de R${} passou a ser R${}'.format(salario, aumento))
elif salario <= 1250:
    decrescimo = (salario*0.15) + salario
    print('O salário de R${} passou a ser R${}'.format(salario, decrescimo))