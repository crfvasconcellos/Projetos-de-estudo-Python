print("Vou analisar se tal ano foi/é Bissexto")
ano= int(input("ANO: "))
anobi= (ano % 4)

if ano % 100 == 0 and ano % 400 == 0:
<<<<<<< Updated upstream:Aulas Curso Em vídeo/Mundo 1 PYTHON/aula010/des 32.py
    print('é bissexto')
else:
    if ano % 100 == 0 and anobi == 0:
        print('não é bissexto')

    else:
        if anobi == 0:
            print("é  um ano bissexto")
=======
    print(é bissexto)
else ano % 400 == 0:
    print("não é bissexto")
>>>>>>> Stashed changes:Aulas Curso Em vídeo/aula010/des 32.py

if