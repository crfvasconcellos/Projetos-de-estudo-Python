print('=' * 10, 'LOJA', '='*10)
pre= float(input('Preços das compras: '))
print('FORMAS DE PAGAMENTO\n [1] À VISTA DINEHIRO/CHEQUE\n [2] À VISTA CRTÃO \n [3] 2X NO CARTÃO\n [4] 3X OU MAIS NO CARTÃO')
op= int(input('Qual é a opção? ')) #lembrar de colocar ele como inteiro

if op == 1:
    pre= pre - (0.1 * pre)
    print('POR PAGAR Á VISTA NO DINHEIRO/CHEQUE, VOCÊ TERÁ 10% DE DESCONTO E PAGARÁ {}'.format(pre))
elif op == 2:
    pre= pre - (0.05 * pre)
    print(f'PELO PAGAMENTO SER À VISTA NO CARTÃO, VOCÊ RECEBERÁ 5% DE DESCONTO, PAGANDO {pre}')
elif op == 3:
    par= pre/2
    print(f'PARCELAREMOS SEU PAGAMENTO DE {pre} EM 2 X DE {par} PELO PREÇO ORIGINAL')
elif op == 4 :
    x = int(input('Quantas vezes você deseja parcelar sua compra (3 ou mais): '))
    if x < 3:
        print('número de parcelas inválidas pela opção escolhida')
    else:
        pre2= (pre + pre * 0.2) / x
        print('VOCÊ PAGARÁ {} PARCELAS DE  {} COM UM JUROS DE 20%'.format(x,pre2))
else:
    print('OPÇÃO INVÁLIDA!')