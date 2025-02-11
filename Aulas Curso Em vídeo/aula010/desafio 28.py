from random import randrange
print("Tente adivinhar em qual número eu pensei de 0 a 5!")
numero = randrange(0,6) #escolhendo um número aleatorio
escolhido= int(input("Qual você acha que é? "))
if escolhido >6 or escolhido <0 :
    print('esse não é um dos números elegiveis')
else:
    if escolhido== numero :
        print("Caramba você conseguiu!!!")
    else:
        print("afe, reinicie o programa e tente novamente")
        print('o número era {}'.format(numero))