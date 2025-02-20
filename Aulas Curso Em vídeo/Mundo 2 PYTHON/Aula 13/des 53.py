print('TESTE DE palíndromo')
frase= str(input('Seu palíndromo: ')).upper().strip()
palavras= frase.split()
junto= ''.join(palavras)
inv= ''
print(junto)
for letras in range(len(junto) - 1,-1,-1):
    inv= inv + junto[letras]

if inv == junto:
    print('A Frase \033[0;32m é um palíndromo\033[m, visto que {} ao contrário é igual {}'.format(junto,inv))
else:
    print('A Frase \033[0;31m não é um palíndromo\033[m, visto que {} ao contrário não é igual {}'.format(junto,inv))