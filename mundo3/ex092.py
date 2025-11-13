import datetime
ano = datetime.date.today().year
dados_trabalhador = {
    "nome": str(input("Nome: ")),
    "ano_nascimento": int(input("Ano nascimento: ")),
    "carteira": int(input("Carteira de Trabalho (0) não tem: "))
}
idade = ano - dados_trabalhador["ano_nascimento"]
if dados_trabalhador["carteira"] == 0:
    print("=-"*30)
    print(f" - NOME TEM O VALOR {dados_trabalhador['nome']}.")
    print(f" - IDADE TEM O VALOR {idade} anos.")
    print(f" - CTPS TEM O VALOR 0.")
else:
    dados_contratacao = {
        "contratação": int(input("Ano de Contratação: ")),
        "salario": float(input("Salário: R$"))
    }
    aposentadoria = idade + (dados_contratacao["contratação"] + 35) - ano
    print("=-" * 30)
    print(f" - NOME TEM O VALOR {dados_trabalhador['nome']}.")
    print(f" - IDADE TEM O VALOR {idade} anos.")
    print(f" - CPTS TEM O VALOR {dados_trabalhador['carteira']}")
    print(f" - APOSENTADORIA TEM O VALOR {aposentadoria} anos.")