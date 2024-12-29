import time
cadastro = "CADASTRE UMA PESSOA"
print("\033[1;34m-\033[m"*30)
print(f"\033[1;34m{cadastro.center(30)}\033[m")
print("\033[1;34m-\033[m"*30)
totpessoas = 0
tothomens = 0
totmulher20 = 0
while True:
    idade = int(input("\033[1;31mIdade:\033[m "))
    sexo =  str(input("\033[1;31mSexo:\033[m ")).lower().capitalize()
    print("\033[1;34m-\033[m" * 30)
    confirmacao = str(input("\033[1;36mQuer continuar? [Sim/Não]:\033[m ")).lower().capitalize()
    print("\033[1;34m-\033[m" * 30)
    if confirmacao == "Sim":
        print("\033[1;34mAGUARDE...\033[m")
        print("\033[1;34m-\033[m" * 30)
        time.sleep(2)
    if idade >= 18:
        totpessoas+=1
    if sexo == 'M':
        tothomens+=1
    if sexo == 'F' and idade < 20:
        totmulher20+=1
    if confirmacao == "Não":
        break
print("\033[1;32mFIM DO PROGRAMA!!!\033[m")
print("\033[1;32mAGUARDE...\033[m")
time.sleep(2)
print(f"Total de pessoas com mais de 18 anos: {totpessoas} pessoas.")
print(f"Ao todo temos {tothomens} homens cadastrados.")
print(f"E temos {totmulher20} mulheres com menos de 20 anos.")