frase = str(input("Digite um frase: ")).lower().strip()

print(f"A letra A aparece {frase.count("a")} vesez na frase.")
print(f"A primeira letra A apareceu na posição {frase.index("a")}")
print(f"A última letra A apareceu na posição {frase.rfind("a")}")