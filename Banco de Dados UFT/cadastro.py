def inserir():
    codigo = input("Codigo: ")
    nome = input("Nome: ")
    saldo = input("Saldo: ")
    valor = input("Valor: ")

    arquivo = open("Banco de Dados UFT\\Produto.txt", "a")
    arquivo.write(codigo + "|" + nome + "|" + saldo + "|" + valor + "\n")
    arquivo.close()

    print("Produto inserido!")


def mostrar_todos():
    arquivo = open("Banco de Dados UFT\\Produto.txt", "r")

    for linha in arquivo:
        print(linha)

    arquivo.close()


def consultar():
    codigo = input("Digite o codigo: ")

    arquivo = open("Banco de Dados UFT\\Produto.txt", "r")

    for linha in arquivo:
        dados = linha.strip().split("|")

        if dados[0] == codigo:
            print("Codigo:", dados[0])
            print("Nome:", dados[1])
            print("Saldo:", dados[2])
            print("Valor:", dados[3])

    arquivo.close()


def deletar():
    codigo = input("Digite o codigo para deletar: ")

    arquivo = open("Banco de Dados UFT\\Produto.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    arquivo = open("Banco de Dados UFT\\Produto.txt", "w")

    for linha in linhas:
        dados = linha.strip().split("|")

        if dados[0] != codigo:
            arquivo.write(linha)

    arquivo.close()

    print("Produto deletado!")


def atualizar():
    codigo = input("Digite o codigo: ")

    arquivo = open("Banco de Dados UFT\\Produto.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    arquivo = open("Banco de Dados UFT\\Produto.txt", "w")

    for linha in linhas:
        dados = linha.strip().split("|")

        if dados[0] == codigo:
            nome = input("Novo nome: ")
            saldo = input("Novo saldo: ")
            valor = input("Novo valor: ")

            arquivo.write(codigo + "|" + nome + "|" + saldo + "|" + valor + "\n")
        else:
            arquivo.write(linha)

    arquivo.close()

    print("Produto atualizado!")


def main():

    while True:

        print("\n--- MENU ---")
        print("1 - Inserir")
        print("2 - Consultar")
        print("3 - Mostrar todos")
        print("4 - Atualizar")
        print("5 - Deletar")
        print("0 - Sair")

        opcao = input("O que deseja fazer? ")

        match opcao:
            case "1":
                inserir()

            case "2":
                consultar()

            case "3":
                mostrar_todos()

            case "4":
                atualizar()

            case "5":
                deletar()

            case "0":
                print("Programa encerrado!")
                break

            case _:
                print("Opcao invalida!")


main()