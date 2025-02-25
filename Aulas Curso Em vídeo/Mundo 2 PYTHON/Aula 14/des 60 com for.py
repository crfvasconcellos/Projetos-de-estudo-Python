print('Calculadora de fatorial!')
num= int(input('Digite um número para calcular seu fatorial: '))
f= 1
print('{}! = '.format(num), end='')
for c in range (num, 0, -1):
    f = f * c
    print('{}'.format(c),end= 'x' if c > 1 else '')
print('=', f)