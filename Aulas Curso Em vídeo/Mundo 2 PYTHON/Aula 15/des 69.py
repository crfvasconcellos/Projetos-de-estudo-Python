c18= 0
ch=0
m20=0
while True:
    print('='*20)
    print('CADASTRE UMA PESSOA!')
    print('='*20)
    idade= int(input('Idade: '))
    while True:
        sexo= str(input('Sexo: [M/F] ')).upper().strip()
        if sexo != 'M' and sexo!= 'F':
            print('Gênero Inválido, Tente novamente!')
        else:
            break
    if idade > 18:
        c18 = c18 + 1
    if sexo == 'M':
        ch = ch + 1
    if sexo == 'F' and idade < 20:
        m20= m20 + 1
    print('-'*20)
    while True:
        desejo= str(input('Quer continuar? [S/N] ')).upper().strip()
        if desejo != 'S' and desejo != 'N':
            print('Opção Inválida, Tente Novamente!')
        else:
            break
    if desejo == 'N':
        break

print('O total de pessoas maiores que 18 anos é {}\nA quantidade de homens cadastrados é {} \nCerca de {} mulheres tem menos de 20 anos'.format(c18,ch,m20))