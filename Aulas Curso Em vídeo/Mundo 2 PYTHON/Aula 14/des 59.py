import time
print('Calculadora!')
dec= 4
dec2= 'S'
while dec == 4 or dec2 == 'S':
    n1= float(input('Primeiro número: '))
    n2= float(input('Segundo número: '))
    dec= int(input('''Digite o que Deseja:
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa '''))
    if dec == 1:
        print('O Resultado é ',n1 + n2)
    elif dec == 2:
        print('O Resultado é', n1 * n2)
    elif dec==3:
        if n1 > n2:
            print('O maior número é', n1)
        elif n2 > n1:
            print('O maior número é', n2)
    elif dec == 5:
        dec2 = 'N'

    if dec != 5 and dec != 4:
        dec2=str(input('Deseja Realizar Outra Operação? [S/N]')).strip().upper()