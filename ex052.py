digite = int(input('Digite um número: '))
tot = 0
for x in range (1, digite+1):
    if digite % x == 0:
        print('\033[0;34m{}\n'.format(x), end=" ")
        tot+=1
    else:
        print('\033[0;35m{}\033[m'.format(x), end=" ")
print('O número {} foi divisel {} vezes'.format(digite, tot))