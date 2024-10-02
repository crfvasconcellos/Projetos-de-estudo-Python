fra= str(input('diga uma frase ')).strip()
print('a letra A aparece {} na frase'.format(fra.count('a')))
print('a primeira letra A apareceu na posição {}'.format(fra.find('a')+1))
print('a ultima letra A apareceu em {}'.format(fra.rfind('a')+ 1))
