import datetime
hj= datetime.date.today().year
qtd= 0
tot= 0
for c in range (1,8):
    nas= int(input(f'Em que ano a {c}º pessoa nasceu? '))
    id= hj - nas
    tot= tot + 1
    if id < 21:
        qtd = qtd + 1
maio= tot - qtd
print(f'Das {tot} pessoas apenas \n{qtd} são menores de idade e \n{maio} são maiores')