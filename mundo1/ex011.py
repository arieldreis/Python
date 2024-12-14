largura = float(input('Largura da Parede: '))
altura = float(input("Qual é a altura da sua parede: "))
area = largura * altura
tinta_litros = area / 2
print(f"Sua parede tem a dimensão de {largura} x {altura} e a sua parede é de {area}m².")
print(f"Para pintar essa parede, você precisará de {tinta_litros}L de Tinta.")