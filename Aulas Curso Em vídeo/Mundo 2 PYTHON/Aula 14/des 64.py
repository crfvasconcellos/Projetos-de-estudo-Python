num= c = s = 0
while num != 999:
    num= int(input("Digite um número [999 para parar]: "))
    if num != 999:
        c= c + 1
        s= s + num
print('Você digitou {} números e a soma entre eles foi {}'.format(c,s))