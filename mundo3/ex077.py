vogais = (
    "APRENDER",
    "PROGRAMAR",
    "LINGUAGEM",
    "PYTHON",
    "CURSO",
    "GRATIS",
    "ESTUDAR",
    "PRATICAR",
    "TRABALHAR",
    "MERCADO",
    "PROGRAMADOR",
    "FUTURO"
)
for p in vogais:
    print(f"Na palavra \033[1;32m{p}\033[m temos as vogais: ", end= "")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f"\033[1;32m{letra}\033[m", end=" ➡️ ")
    print()