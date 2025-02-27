print('CALCULADOR DE TABUADA!!')
num= 0
m= 1
while True:
    num = int(input('Deseja Ver a Tabuada de Qual valor? '))
    if num < 0:
        break
    m = 1
    r = 0
    print('-'*10)
    while True:
        if m>10:
            break
        print(f'{num} x {m} é {num*m}')
        m= m + 1
    print('-'*10)
print('PROGRAMA DE TABUADA ENCERRADO, VOLTE SEMPRE!!')
