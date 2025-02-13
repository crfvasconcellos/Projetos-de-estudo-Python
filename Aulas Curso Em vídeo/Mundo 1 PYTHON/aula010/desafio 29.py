from time import sleep
velo= int(input("A qual velocidade está este carro? (velocidade max é 80 km/h"))
print("verificando...")
multa=0
sleep(2)
if velo>80:
    print('você está acima da velocidade permitida')
    multa= (velo-80)* 7
    print("sua multa será de aproximadamente {} reais".format(multa))
else:
    print("você esta dentro da velocidade permitida.")
