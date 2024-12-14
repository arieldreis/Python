# Curso de Python básico da hashtag
# ‘Loop’ e Estruturas de Repetição

lista_vendas = [1000, 500, 800, 1500, 2000, 2300]

metas = 1200
percentual_bonus = 0.1

for vendas in lista_vendas:
   if vendas >= metas:
       bonus = percentual_bonus * vendas
   else:
       bonus = 0
   print(bonus)