print('Calcularei seu IMC(Índice de Massa Corporal) e falarei o seu status')
peso= float(input('QUAL O SEU PESO? (KG) '))
alt= float(input('QUAL É A SUA ALTURA? (M) '))

imc= peso/ (alt ** 2)

if imc < 18.5:
    print('VOCÊ ESTA ABAIXO DO PESO, COM UM IMC DE {}'.format(imc))
elif 18.5 <= imc < 25:
    print('VOCÊ ESTA NO PESO IDEAL COM IMC DE {}'.format(imc))
elif 25 <= imc < 30:
    print('VOCÊ ESTA COM SOBREPESO, COM UM IMC DE {}'.format(imc))
elif 30 <= imc <= 40:
    print('VOCÊ POSSUI OBESIDADE, COM UM IMC DE {}'.format(imc))
elif 40 < imc:
    print('VOCÊ POSSUI OBESIDADE MÓRBIDA, COM UM IMC DE {}'.format(imc))