print('Descobridor de números primos')

num = int(input('Digite um número: '))
print(f'Digite um número: \033[0;32m{num}\033[m')  # Número digitado em verde

tot = 0  # Contador de divisores

# Laço para verificar os divisores
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[0;33m{c}\033[m', end=' ')  # Amarelo para divisores
        tot += 1
    else:
        print(f'\033[0;31m{c}\033[m', end=' ')  # Vermelho para não divisores

# Exibir o total de divisores em azul
print(f'\nO número {num} foi divisível \033[0;34m{tot}\033[m vezes')

# Verificar se é primo ou não
if tot > 2 or tot == 1:
    print(f'{num} \033[0;31mNÃO\033[m é um número primo!')
else:
    print(f'{num} \033[0;32mÉ UM NÚMERO PRIMO!\033[m')
