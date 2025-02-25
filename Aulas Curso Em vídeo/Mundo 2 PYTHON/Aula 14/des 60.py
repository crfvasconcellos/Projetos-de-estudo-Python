print('Calculadora de fatorial!')
num= int(input('Digite um número para calcular seu fatorial: ')) + 1
f= 1
print('{}!= '.format(num - 1), end= '')
while num > 1:
    num= num - 1
    f= f * num
    print('{}'.format(num),end=' x ' if num> 1 else '')

print(' =', f)
print('O Resultado é {}'.format(f))

