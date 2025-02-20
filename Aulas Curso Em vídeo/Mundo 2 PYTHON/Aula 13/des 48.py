print('Calcularei a soma entre todos os múltiplos de 3  entre 1 e 500')
s= 0
cont= 0

for c in range (1,501,2):
    if c % 3 == 0:
        s= s + c
        cont= cont + 1

print('A SOMA DOS  {} NÚMEROS IMPARES MÚLTIPLOS DE 3 É {}'.format(cont,s))