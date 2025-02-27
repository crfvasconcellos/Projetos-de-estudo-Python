print('CALCULADOR DE TABUADA!!')
num= 0
m= 1
r=0
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
        r= m * num
        print(f'{num} x {m} é {r}')
        r= 0
        m= m + 1
    print('-'*10)
print('PROGRAMA DE TABUADA ENCERRADO, VOLTE SEMPRE!!')
