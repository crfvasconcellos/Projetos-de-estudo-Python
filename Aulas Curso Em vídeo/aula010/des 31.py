print("Qual a distância da sua viagem?")
dis= int(input("Distância (em km): "))
if dis <= 200:
    val= 0.5 * dis
    print("a sua passagem custará {}".format(val))
else:
    val= 0.45 * dis
    print("vc teve desconto, a sua passagem custará {}".format(val))
