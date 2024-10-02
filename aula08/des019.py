import random
n1 = input("primeiro aluno: ")
n2 = input("segundo aluno: ")
n3 = input("terceiro aluno: ")
n4 = input("quarto aluno: ")
lista = [n1,n2,n3,n4]
escol= random.choice(lista)
print ("o aluno foi {}" .format(escol))