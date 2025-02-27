import random
s=cont=0
numero=desejobot=m=' '
print('PAR OU ÍMPAR BOT!!!')
print('-'*20)
while True:
    c = random.randint(1, 10)
    n= int(input('Digite um Valor: '))
    desejo= str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    soma= n +  c
    #verificando total
    if soma % 2 == 0:
        numero='P'
        m= 'PAR'
    else:
        numero='I'
        m= 'ÍMPAR'
    print('=-'*30)
    print('Você Jogou {} e o Bot jogou {}, a soma é {}, sendo {}'.format(n,c,soma,m))
    print('=-'*30)
    if desejo =='P':
        desejobot='I'
    else:
        desejobot='P'

    if desejo == numero:
        print('Você Ganhou!!!')
        cont= cont+1
        print('Vamos jogar denovo...')
        print('-'*20)
    else:
        print('O Bot Ganhou!!')
        break
print('GAME OVER, VOCÊ VENCEU {} PARTIDAS!'.format(cont))
