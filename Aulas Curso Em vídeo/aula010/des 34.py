print("Vamos Calcular o seu aumento!!!")
sal1= float(input("Quanto voce recebe agora? "))
sal2= 0
if sal1 > 1250.0 :
    sal2 = ((sal1 / 100) * 10) + sal1
    au= ('10%')
if sal1 <= 1250.0:
    sal2= ((sal1 / 100 ) * 15) + sal1
    au= ("15%")

print("Seu novo salário é {} e recebeu um aumentou de {}".format(sal2, au))
