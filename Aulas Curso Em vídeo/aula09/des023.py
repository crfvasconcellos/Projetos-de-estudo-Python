num= int(input('diga um número até 9999 : '))
u= num % 10
d= num//10 % 10
c= num//100 % 10
m= num//1000 % 10
#num1 = num[3]
#num2= num[2]
#num3= num[1]
#num4= num[0]

print('ele tem:')
print('{} unidades'.format(u))
print('{} dezenas '. format(d) )
print('{} centenas'.format(c))
print('{} milhar'.format(m))