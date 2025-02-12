print("Vou analisar se tal ano foi/é Bissexto")
ano= int(input("ANO: "))
anobi= (ano % 4)

if ano % 100 == 0 and ano % 400 == 0:
    print(é bissexto)
else ano % 400 == 0:
    print("não é bissexto")

if ola