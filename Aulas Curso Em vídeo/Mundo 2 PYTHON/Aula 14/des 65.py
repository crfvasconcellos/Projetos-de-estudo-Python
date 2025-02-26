num= med= maior = menor= soma = count= 0
desejo ='S'

while desejo == 'S':
    num= int(input('Digite um número: '))
    soma= soma + num
    count= count + 1
    if count == 1:
        maior = num
        menor= num
    if num > maior:
        maior= num
    elif num < menor:
        menor= num
    desejo= str(input('Quer Continuar? [s/n] ')).upper().strip()
    if desejo == 'N':
        med= float(soma/count)

print('Você digitou {} números e a média foi {}\nO maior valor foi {} e o menor foi {}'.format(count,med,maior,menor))