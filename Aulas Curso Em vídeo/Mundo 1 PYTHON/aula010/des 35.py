print("Me diga o valor de 3 retas e eu verificarei se elas podem formar um Triangulo!")
r1= float(input("Reta 1: "))
r2= float(input("Reta 2: "))
r3= float(input("Reta 3: "))
c1 = 0
c2 = 0
c3 = 0
if r1 + r2 > r3:
    c1= ('ok')

if r1 + r3 > r2:
    c2= ('ok')

if r2 + r3 > r1:
    c3= ('ok')

if c1 == 'ok' and c2 == 'ok' and c3 == 'ok':
    print("eles podem ser um triângulo")
else:
    print("Não podem formar um triângulo")