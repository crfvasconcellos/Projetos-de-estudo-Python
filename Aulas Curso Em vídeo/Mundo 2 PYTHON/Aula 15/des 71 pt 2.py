print('=-'*30)
print('CAIXA ELETRÔNICO')
print('=-'*30)

cel=50
qtd= 0
valsac=int(input('Qual o valor a ser sacado? R$'))
valorat=valsac
while True:
    while valorat > 0:
        qtd= valorat//cel
        valorat= valorat - (qtd*cel)

        if qtd>0:
            print('Total de {} cédulas de R${}'.format(qtd,cel))

        if cel == 50:
            cel=20
        elif cel == 20:
            cel=10
        elif cel == 10:
            cel= 1
        if valorat == 0:
            break

print('=-' * 30)
print('Volte Sempre!!!')