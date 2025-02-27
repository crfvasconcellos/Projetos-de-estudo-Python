print('=-'*30)
print('CAIXA ELETRÔNICO')
print('=-'*30)

#Cédulas
qcin=qvin=qdez=qum= 0
valorat=0


valsac=int(input('Qual o valor a ser sacado? R$'))

if (valsac // 50) >=1:
    qcin= valsac//50
    valorat= valsac - (qcin*50)
    print('Total de {} cédulas de R$50'.format(qcin))
if (valorat//20) >=1:
    qvin= valorat//20
    valorat= valorat - (qvin*20)
    print('Total de {} cédulas de R$20'.format(qvin))
if (valorat//10) >=1:
    qdez= valorat//10
    valorat= valorat - (qdez*10)
    print('Total de {} cédulas de R$10'.format(qdez))

if (valorat//1) >= 1:
    qum= valorat//1
    valorat= valorat - qdez
    print('Total de {} cédulas de R$1'.format(qum))

print('=-' * 30)
print('Volte Sempre!!!')