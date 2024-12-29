while True:
    tabuada = int(input("\033[1;34mDigite um número:\033[m "))
    if tabuada <= 0:
        print("\033[4;33mPROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!\033[m")
        break
    else:
        cont = 1
        resultado = ""
        while cont <= 10:
            multiplication = cont * tabuada
            resultado+=f"{tabuada} x {cont} = {multiplication}\n"
            cont+=1
        print("\033[1;34m-\033[m" * 30)
        print(f"{resultado}")
        print("\033[1;34m-\033[m" * 30)