print('-'*10)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*10)

n1=0
n2=1
n3=0
count = 0
qtd= int(input('Quantos Termos você deseja mostrar: '))

print('=-'*10)
while count != qtd :
    if count == 0:
        print(n1, end=' -> ')
        count = count + 1
    if count== 1 and count != qtd:
        print(n2, end=' -> ')
        count = count + 1

    if count != qtd:
        n3 = n1 + n2
        print(n3, end=' -> ')
        count = count + 1
    if count != qtd:
        n1 = n2 + n3
        print(n1, end=' -> ')
        count = count + 1
    if count != qtd:
        n2= n1 + n3
        print(n2, end=' -> ')
        count = count + 1
    if count == qtd:
        print('FIM')
print('=-'*10)