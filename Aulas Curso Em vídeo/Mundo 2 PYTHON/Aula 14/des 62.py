print('-='* 10)
print('Gerador de PA de 10 termos')
print('-='* 10)
desejo = 'N'
n1= int(input('Primeiro Termo: '))
raz= int(input('Razão: '))
n2= n1 + (raz * 9)
qtd= 9
c= 0
count= 0
print(f'{n1} -> ', end='')
while n1 != n2 :
    n1= n1 + raz
    print('{}'.format(n1), end=' -> ' if n1 != n2 else ' -> Pausa')
    c= c + 1
    count = count + 1
    if c== qtd:
        print()
        desejo = str(input('Deseja Mostrar mais termos dessa PA? [s/n] ')).upper().strip()
        if desejo == 'S':
            qtd = int(input('Quantos termos você quer mostrar a mais? '))
            n2 = n1 + (raz * qtd)
            c= 0

print('Projeção finalizada com {} termos mostrados'.format(count + 1))