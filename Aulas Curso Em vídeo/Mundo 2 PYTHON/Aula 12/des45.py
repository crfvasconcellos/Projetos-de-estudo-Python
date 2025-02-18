import random
import time
print('\033[0;36m=\033[m'*10,'\033[0;33mJokenpô\033[m', '\033[0;36m=\033[m'*10)
print('''SUAS OPÇÕES:
[1] PEDRA
[2] PAPEL 
[3] TESOURA''')
op= str(input('Qual sua opção? ')).strip()
lista= ['PEDRA', 'PAPEL', 'TESOURA']
opc= random.choice(lista)


#ajeitando as opções
if op == '1':
    op = 'PEDRA'
elif op == '2':
    op = 'PAPEL'
elif op == '3':
    op = 'TESOURA'
else:
    print('\033[0;31mSUA OPÇÃO FOI INVÁLIDA')

if op == 'PEDRA'or op == 'PAPEL' or op == 'TESOURA':
    time.sleep(1)
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!!')
    print( '-=' * 15 )
    print(f'O COMPUTADOR ESCOLHEU {opc}')
    print(f'VOCÊ ESCOLHEU {op}')
    print( '-=' * 15 )

    #Comparando as opções
    if opc == op:
        print('EMPATOU!')
    elif op == 'PEDRA' :
        if opc == 'PAPEL':
            print('O PC GANHOU!')
        else:
            print('VOCÊ GANHOU!')
    elif op == 'PAPEL':
        if opc == 'TESOURA':
            print('O PC GANHOU!')
        else:
            print('VOCÊ GANHOU!')
    elif op == 'TESOURA':
       if opc == 'PEDRA':
            print('O PC GANHOU!')
       else:
            print('VOCÊ GANHOU!')


