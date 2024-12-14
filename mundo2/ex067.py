cont = 0
while True:
    tabuada = int(input("\033[1;34mDigite um número:\033[m "))
    if tabuada <= 0:
        print("\033[4;33mPROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!\033[m")
        break
    while cont <= 10:
        cont+=1
        multiplicacao = cont * tabuada
        print("\033[1;34m-\033[m" * 30)
        print(f"{tabuada} x {cont} = {multiplicacao}")
        print("\033[1;34m-\033[m" * 30)
        cont+=1