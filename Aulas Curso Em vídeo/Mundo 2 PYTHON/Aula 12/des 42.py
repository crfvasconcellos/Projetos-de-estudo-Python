print('Detector de Formação de Triângulos com retas')
l1= float(input('Primeiro segmento: '))
l2= float(input('Segundo segmento: '))
l3= float(input('Terceiro segmento: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2 :
    print('É POSSÍVEL FAZER UM TRIÂNGULO COM ESTAS RETAS')
    if l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('este seria um triângulo ISÓSCELES')
    elif l1 == l2 == l3:
        print('este seria um triângulo EQUILÁTERO')
    else:
        print('este seria um triângulo ESCALENO')
else:
    print('NÃO É POSSÍVEL FAZER UM TRIÂNGULO COM ESSES SEGMENTOS')