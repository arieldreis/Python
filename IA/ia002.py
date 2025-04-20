import pandas as pd
# É usada pra tabelas, igual no Excel, mas no Python.
# A estrutura principal é o DataFrame, que parece uma planilha.
dados = {
    "nome":["Ana", "João"],
    "idade": ["20", "25"]
}
df = pd.DataFrame(dados)
print(df)