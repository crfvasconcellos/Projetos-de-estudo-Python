n=1
c=0
p=0
while n!=0:
    n= int(input('Digite um Número (0 para cancelar): '))

    #ímpares
    if n % 2 != 0:
        c= c +1
    #Pares
    else:
        p= p+1

print(f'Você digitou {c} números ímpares e {p} números pares')