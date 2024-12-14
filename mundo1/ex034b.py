def mensao(nota1, nota2, nota3,nota4):
    return ((nota1 + nota2+nota3+nota4)/4)
nota1 = float(input('Digite a primeira mensão:'))
nota2 = float(input('Digite a segunda mensão:'))
nota3 = float(input('Digite a terceira mensão:'))
nota4 = float(input('Digite a quarta mensão:'))
if mensao(nota1, nota2, nota3,nota4) > 9.0:
    print(f'Analisando ás suas mensões, podemos concluir que a sua nota será {mensao(nota1, nota2, nota3,nota4)} resultando em um \033[0;34mMB\033[m')
elif mensao(nota1, nota2, nota3,nota4) < 9.0 and mensao(nota1, nota2, nota3,nota4) > 7.5:
    print(f'Analisando ás suas mensões, podemos concluir que a sua nota será {mensao(nota1, nota2, nota3,nota4)} resultando em um \033[0;32mB\033[m')
elif mensao(nota1, nota2, nota3,nota4) < 7.5 and mensao(nota1, nota2, nota3,nota4) > 6.0:
    print(f'Analisando ás suas mensões, podemos concluir que a sua nota será {mensao(nota1, nota2, nota3,nota4)} Resultando em \033[0;33mR\033[m')
elif mensao(nota1, nota2, nota3,nota4) < 6.0 and mensao(nota1, nota2, nota3,nota4) > 4.0:
    print(f'Analisando ás suas mensões, podemos concluir que a sua nota será {mensao(nota1, nota2, nota3,nota4)} Resultando em um \033[0;91mI\033[m')
else:
    print(f'Analisando ás suas mensões, podemos concluir que a sua nota será {mensao(nota1, nota2, nota3,nota4)} Resultando em um \033[0;97mNA\033[m')