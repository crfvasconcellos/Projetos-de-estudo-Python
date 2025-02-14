num= int(input('DIGITE UM NÚMERO INTEIRO: '))
print('ESCOLHA UMA DAS BASES DE CONVERSÃO:\n(1)BINÁRIA\n(2)OCTAL\n(3)HEXADECIMAL')
esc= int(input('Sua opção: '))


if esc== 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif esc== 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif esc==3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print(' ESTA NÃO É UMA DAS OPÇÕES VÁLIDAS')