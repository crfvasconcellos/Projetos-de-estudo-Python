import datetime
print('Irei analisar quando você deve se alistar')
ano= int(input('EM QUE ANO VOCÊ NASCEU: '))
hoje= str(datetime.date.today())
hoje= int(hoje[:4])
ida= hoje - ano
if ida == 18:
    print('VOCÊ SE ALISTARÁ ESSE ANO')
elif ida < 18:
    fal= 18 - ida
    ano2= hoje + fal
    print("VOCÊ AINDA TEM TEMPO PARA SE ALISTAR, FALTAM {} ANOS\nE VOCÊ SE ALISTARÁ EM {}".format(fal,ano2))
elif ida > 18:
    fal= ida - 18
    ano2 = hoje - fal
    print('PASSOU O SEU PRAZO DE SE ALISTAR HÁ {} ANOS\nE VOCÊ SE ALISTOU EM {}'.format(fal, ano2))
