print('Me fale 3 números e eu falarei qual é maior e qual é menor')
n1= float(input('Número 1: '))
n2= float(input('Número 2: '))
n3= float(input('Número 3: '))
#Verificando o menor valor
menor= n1
maior= n3
if n2< n1 and n2< n3:
    menor= n2
if n3 < n1 and n3 < n2:
    menor= n3

print('menor = {}'.format(menor))
#verificando o maior valor

if n1 > n3 and n1 > n2:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2

print('O maior valor = {}'.format(maior))