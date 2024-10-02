nome= input('digite o seu nome: ').strip()
nome=  nome.split()
print('seu primeiro nome é {}'.format(nome[0]))
print('seu último nome é {}'.format(nome[len(nome)-1]))