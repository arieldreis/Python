expressao = str(input("Digite a expressao:"))
pilha = []
for x in expressao:
    if x == "(":
        pilha.append("(")
    elif x == ")":
        pilha.append(")")
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressão está valida.")
else:
    print("Sua expressão está invalida.")