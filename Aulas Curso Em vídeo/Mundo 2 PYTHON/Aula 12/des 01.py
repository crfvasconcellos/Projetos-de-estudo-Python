print('\033[35m-='*20)
print('ANALISADOR DE EMPRÉSTIMO BANCÁRIO DE CASAS')
print('-='*20)
val= int(input("\033[mValor da casa desejada: "))
sal= int(input("Seu salário: "))
anos= int(input("Em quantos anos você pretende pagar: "))
meses= anos * 12
prest= val/meses

if prest > ((sal/100) * 30):
    print(f"Para pagar uma casa de {val} em {anos} a prestação será {prest}")
    print('Não poderemos liberar este empréstimo')
else:
    print(f'liberaremos o seu empréstimo e você terá que pagar {meses} parcelas de {prest}')
