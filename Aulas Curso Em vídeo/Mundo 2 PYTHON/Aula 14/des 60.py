print('Calculadora de fatorial!')
num= int(input('Digite um número para calcular seu fatorial: '))
a= 1
b= ''
while b != 'OK':
        num= num -1
        a= a * num
        print(' {} '.format(num), end='x' if num > 1 else '')


print('=',a)
print('O Resultado é', a)

