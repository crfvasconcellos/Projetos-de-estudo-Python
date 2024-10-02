print("bem-vindo ao calculador de tinta!")
l= float(input("qual é a largura da sua parede em m? "))
a= float(input("qual a altura da sua parede? "))
area= a*l
tinta= area/2
print("para pintar uma parede com {} m2 vc precisará de {} l de tinta!".format(area,tinta))