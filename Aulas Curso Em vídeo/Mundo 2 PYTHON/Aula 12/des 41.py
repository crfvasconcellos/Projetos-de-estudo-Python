from datetime import date
print('ANALISAREMOS A SUA IDADE E TE COLOCAREMOS EM SUA CATEGORIA RESPECTIVA')
hj= date.today().year
nas= int(input('Em que ano Você nasceu:'))
ida= hj - nas

if ida <= 9:
    print('VOCÊ ESTÁ CLASSIFICADO COMO UM ATLETA MIRIM')
elif ida <= 14:
    print('VOCÊ ESTÁ CLASSIFICADO COMO UM ATLETA INFANTIL')
elif ida <= 19:
    print('VOCÊ ESTÁ CLASSIFICADO COMO UM ATLETA JÚNIOR')
elif ida <= 25:
    print('VOCÊ ESTÁ CLASSIFICADO COMO UM ATLETA SÊNIOR')
elif ida > 25:
    print('VOCÊ ESTÁ CLASSIFICADO COMO UM ATLETA MASTER')
