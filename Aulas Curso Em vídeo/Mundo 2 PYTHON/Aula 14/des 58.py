import random
c= 1
r= ''
print('''Sou seu Computador...
Acabei de pensar em um número entre 0 e 10.
Será que Você consegue adivinhar qual foi?''')

while r != 'n':
    num= random.randint(1,10)
    p= int(input('Qual o seu palpite: '))
    if p == num:
        print('Parabéns!!! Você acertou de primeira!')
    elif p != num:
        while p != num:
            if p < num:
                print('mais...')
            elif p > num:
                print('menos...')
            p= int(input('humm, não é esse, tente novamente! Palpite: '))
            c= c + 1
            if p == num:
                print('Você Conseguiu!!!')

    print('Você demorou {} tentativas para acertar o número pensado({})'.format(c,num))
    r= input('Deseja Jogar Novamente? [s/n] ').strip().lower()