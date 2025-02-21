#Acumuladores
idades= 0
maior= 0
nmaior= ''
contm= 0

for c in range (1,5):
    print(f'---- {c}º PESSOA ----')
    #Perguntas
    nom=str(input('Qual o seu nome? ')).strip()
    ida= int(input('Qual sua idade?'))
    sex= str(input('Seu Sexo é Masculino ou feminino?(m/f) ')).lower().strip()

#Cálculo idade Masculina
    if ida < 0:
        print('Idade Inválida')
    else:
        if c == 1:
            maior= ida
            nmaior= nom

        if ida > maior and sex == 'm':
            maior = ida
            nmaior= nom

    #Cálculo mulheres
    if  sex == 'f' and ida < 20:
        contm= contm + 1



#calculo idades
    idades= idades + ida
idades= idades/4

#Respostas do desafio
print('A Média das Idades das 5 Pessoas é {}'.format(idades))
print('A idade do maior Homem ({}) é {} anos'.format(nmaior,maior))
print('O Número de Mulheres com Menos de 20 Anos é {}'.format(contm))