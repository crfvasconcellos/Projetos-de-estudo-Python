print('Calculadora!')
dec= 0
dec2= ''
cond= 0
cond2 = 0
while cond== 0:
    n1= float(input('Primeiro número: '))
    n2= float(input('Segundo número: '))
    cond2=0
    while cond2== 0:
        dec= int(input('''Digite o que Deseja:
    [ 1 ] somar
    
    [ 2 ] multiplicar
    
    [ 3 ] maior
    
    [ 4 ] novos números
    
    [ 5 ] sair do programa '''))
        if dec == 1:
          print('O Resultado é', n1 + n2)
        elif dec == 2:
            print('O Resultado será', n1 * n2)
        elif dec == 3:
            if n1 > n2:
                print('O maior número é', n1)
            elif n2 > n1:
                print('O maior número é', n2)
            else:
                print('Ambos são iguais!')
        elif dec == 4:
            print('Remudando opções!')
            cond2= 1
        elif dec == 5:
            print('saindo!')
            cond=1
            cond2= 1
        else:
            print('Opção Inválida, tente Novamente!')
        if dec == 1 or dec==2 or dec == 3:
            dec2= str(input('Deseja fazer outro tipo de conta? [s/n] ')).upper().strip()
            if dec2 == 'N':
                cond= 1
                cond2= 1

print('Programa Finalizado!')