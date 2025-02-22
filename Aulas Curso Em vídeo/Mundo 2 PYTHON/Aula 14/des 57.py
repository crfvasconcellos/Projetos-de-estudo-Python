sex = str(input('Informe o seu sexo: [M/F] ')).lower().strip()
c = 0

while sex != 'm' and sex != 'f':
    sex= str(input('Dados Inválidos. Por favor, informe o seu sexo [M/F] ')).lower().strip()


if sex == 'm':
    sex = 'masculino'
elif sex == 'f':
     sex = 'feminino'
print('Você é do sexo {}'.format(sex))