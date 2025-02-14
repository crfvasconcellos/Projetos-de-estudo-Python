from datetime import date
print('Irei analisar quando você deve se alistar')
sex= str(input('Primeiramente, você é do sexo MASCULINO(M) ou FEMININO(F): ')).upper()
if sex == 'F':
    print('MULHERES NÃO PRECISAM SE ALISTAR NO BRASIL!')
elif sex != 'F' and sex != 'M':
    print('ESTA NÃO É UMA OPÇÃO VÁLIDA, REINICIE O PROGRAMA!')
else:
    ano= int(input('EM QUE ANO VOCÊ NASCEU: '))
    hoje= str(date.today())
    hoje= int(hoje[:4])
    ida= hoje - ano
    if ida == 18:
        print('VOCÊ SE ALISTARÁ ESSE ANO')
    elif ida < 18:
        fal= 18 - ida
        ano2= hoje + fal
        print("VOCÊ AINDA TEM TEMPO PARA SE ALISTAR, FALTAM {} ANO(S)\nE VOCÊ SE ALISTARÁ EM {}".format(fal,ano2))
    elif ida > 18:
        fal= ida - 18
        ano2 = hoje - fal
        print('PASSOU O SEU PRAZO DE SE ALISTAR HÁ {} ANO(S)\nE VOCÊ SE ALISTOU EM {}'.format(fal, ano2))
