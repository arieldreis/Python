def area(l, c):
    area = largura * comprimento
    print(f"A área de um terreno {largura} x {comprimento} é de {area:.2f}m²")

largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area(largura, comprimento)