soma= 0
cont= 0
for a in range(1,7):
    n= int(input('Número {} º: '.format(a)))
    if n % 2 != 0:
        print('Desconsiderado!')

    else:
        soma= soma + n
        cont= cont + 1

print('A soma dos  {} números pares é igual à {}'.format(cont,soma))
