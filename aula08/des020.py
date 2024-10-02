import random
n1= input("primeiro aluno: ")
n2= input("segundo aluno: ")
n3= input("terceiro aluno: ")
n4= input("Quarto aluno: ")
lista= [n1,n2,n3,n4]
random.shuffle(lista)
print ("a ordem será")
print(lista)