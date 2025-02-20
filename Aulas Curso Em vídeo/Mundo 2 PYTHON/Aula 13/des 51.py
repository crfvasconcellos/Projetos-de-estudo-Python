print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

t=int(input('Primeiro Termo: '))
raz= int(input('Razão: '))
d= t + (10-1) * raz
for c in range(t ,raz+d,raz):
    print(c, end= '→')
print('Acabou')
