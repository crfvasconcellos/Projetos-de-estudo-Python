print('-='* 10)
print('Gerador de PA de 10 termos')
print('-='* 10)
vez = 1
n1= int(input('Primeiro Termo: '))
raz= int(input('Razão: '))
n2= n1 + (raz * 9)
print(f'{n1} -> ', end='')
while n1 != n2:
    n1= n1 + raz
    print('{}'.format(n1), end=' -> ' if n1 != n2 else ' -> FIM')