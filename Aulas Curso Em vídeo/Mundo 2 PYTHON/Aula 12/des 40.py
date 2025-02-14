print('CALCULAREI SUAS DUAS MÉDIAS DA PROVA')
not1= float(input('NOTA 1: '))
not2= float(input('NOTA 2: '))
med= (not1+not2)/2
if med >= 7:
    print('PARABÉNS, VOCÊ FOI APROVADDO COM UMA MÉDIA DE {} PONTOS'.format(med))
elif 5 <= med <= 6.9:
    print('VOCÊ IRÁ PARA A RECUPRERAÇÃO COM SUA MÉDIA DE {} PONTOS'.format(med))
elif not1 + not2 > 20:
    print('NOTAS INVALIDAS, REINICIE O PROGRAMA')
else:
    print('VOCÊ FOI REPROVADO COM UMA MÉDIA DE {} PONTOS'.format(med))