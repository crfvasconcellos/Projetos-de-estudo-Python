print('ME DIGA DOIS NÚMEROS E VOU COMPARA-LOS')
n1 = float(input('PRIMEIRO NÚMERO: '))
n2 = float(input('SEGUNDO NÚMERO: '))
if n1 > n2:
    print('DEFINITIVAMENTE {} É MAIOR QUE {}'.format(n1,n2))
elif n2 > n1:
    print('DEFINITIVAMENTE {} É MAIOR QUE {}'.format(n2, n1))

elif n1 == n2:
    print('ELES DEFINITIVAMENTE SÃO IGUAIS')