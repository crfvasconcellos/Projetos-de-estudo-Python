n=c=s=0

while True:
    n= int(input('Digite Um valor [999 para Parar]: '))
    if n== 999:
        break
    s= s + n
    c= c + 1
print('Acabou!')
print(f'Você Digitou {c} números e a soma deles foi {s}')