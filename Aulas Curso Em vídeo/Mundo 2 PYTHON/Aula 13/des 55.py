print('Comparador de pesos\n')
menor= 0
maior= 0

for c in range(1,6):
    peso= float(input(f'Peso da {c}º pessoa: '))
    menor = peso
    if peso > maior:
        maior = peso

    if peso < menor:
        menor= peso


print('DAS 5 PESSOAS, O MAIOR PESO FOI {} E O MENOR FOI {}'.format(maior,menor))

