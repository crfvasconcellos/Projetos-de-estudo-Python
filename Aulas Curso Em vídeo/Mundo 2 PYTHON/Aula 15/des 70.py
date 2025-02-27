print('='*30)
print('LOJA DO CLAUDIO!')
print('='*30)
desejo=''
nmenor= ' '
pmenor= 0
c1000=0
totalg=0
c=0
while True:
    produto= str(input('Nome do Produto: '))
    preço= int(input('Preço: R$'))
    if c==0:
        nmenor= produto
        pmenor= preço
    c=c+1
    if preço < pmenor:
        nmenor= produto
        pmenor= preço
    totalg= totalg + preço

    if preço>1000:
        c1000= c1000 + 1
    while True:
        desejo= str(input('DESEJA CONTINUAR? [S/N] ')).upper().strip()
        if desejo != 'S' and desejo != 'N':
            print('Valor Inválido, Tente novamente! ')
        else:
            break
    if desejo == 'N':
        break

print('Programa finalizado!\nO gasto Total foi R${}\n{} produtos custam mais de R$1000\nO produto mais barato é {} custando R${}'.format(float(totalg),c1000,nmenor,pmenor))