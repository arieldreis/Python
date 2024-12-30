bqnco = "\033[1;36mBANCO CEV\033[m"
print("\033[3;36m=\033[m"*40)
print(bqnco.center(50))
print("\033[3;36m=\033[m"*40)
caixa = int(input("\033[1;36mQual é o valor que você quer sacar? R$\033[m"))
total = caixa
cedula = 100
totcedula = 0
while True:
    if caixa < 20:
        print("\033[1;37m=\033[m" * 50)
        print("\033[1;31mO VALOR QUE VOCÊ ESTÁ PEDINDO É MUITO BAIXO!\033[m")
        print("\033[1;31mO VALOR MINÍMO É DE 20 REAIS!\033[m")
        break
    elif caixa > 1000:
        print("\033[1;37m=\033[m" * 50)
        print("\033[1;31mO VALOR QUE VOCÊ ESTÁ PEDINDO É MUITO ALTO!\033[m")
        print("\033[1;31mO SAQUE MÁXIMO É DE ATÉ 1000 REAIS!\033[m")
        break
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print("\033[1;32m=\033[m" * 50)
            print(f"\033[1;32mTOTAL DE {totcedula} CÉDULAS DE R${cedula}\033[m")
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print("\033[1;32m=\033[m"*50)
print("OBRIGADO POR CONTATAR COM O BANCO CEV")