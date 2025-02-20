import time
print('Contagem regressiva!!!!!!')
d= input('Deseja começar a contagem? (s/n) ').lower().strip()
if d == 'n':
    print('Programa Encerrado')
elif d == 's':
    for a in range(10,0,-1):
        time.sleep(1)
        print(a)
print('Os fogos Começaram!!!!!')