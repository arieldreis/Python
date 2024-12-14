produto = float(input("Qual é o preço do produto:R$"))
desconto = produto - (produto * 0.05)
print(f"O produto que custava R${produto}, na promoção com 5% vai custar R${round(desconto, 2)}")