import datetime
import time
trabalhador  = {
    "nome": str(input("Nome: ")),
    "idade": int(input("Idade: ")),
    "carteira_trabalho": int(input("Carteira de Trabalho (0 não tem): "))
}
if trabalhador["carteira_trabalho"] == 0:
    print(f" - Nome tem o valor {trabalhador['nome']}")
    print(f" - Idade tem o valor {trabalhador['idade']} anos")
    print(f" - CTPS tem o valor {trabalhador['carteira_trabalho']}")
else:
    trabalhador["contratacao"] = int(input("Ano de Contratação: "))
    trabalhador["salario"] = float(input("Salário: R$"))
    # Respostas finais
    trabalhador['ano'] = ano = datetime.datetime.now().year
    trabalhador["aposentadoria"] = trabalhador["idade"] + ((trabalhador["contratacao"] + 35) - trabalhador['ano'])

'''DADOS FINAIS DO RESULTADO'''
print(f" - Nome tem o valor {trabalhador['nome']}")
print(f" - Idade tem o valor {trabalhador['idade']} anos")
print(f" - CTPS tem o valor {trabalhador['carteira_trabalho']}")
print(f" - Contratação tem o valor {trabalhador['contratacao']}")
print(f" - Salário tem o valor de R${trabalhador['salario']}")
print(f" - Aposentadoria tem o valor {trabalhador['aposentadoria']} anos")
