# Nome dos estudantes: Mickaell e Luis F.
# Turma: 1BTI

# ==========================================
# PROJETO FINAL - CATALOGO DE FILMES
# ==========================================

# Lista com os filmes ja cadastrados
filmes = [
    {
        "codigo": 101,
        "titulo": "Harry Potter e a Pedra Filosofal",
        "genero": "Fantasia",
        "ano": 2001,
        "nota": 7.9
    },
    {
        "codigo": 102,
        "titulo": "As Cronicas de Narnia: O Leao, a Feiticeira e o Guarda-Roupa",
        "genero": "Fantasia",
        "ano": 2005,
        "nota": 7.5
    },
    {
        "codigo": 103,
        "titulo": "Vingadores",
        "genero": "Acao",
        "ano": 2012,
        "nota": 8.0
    }
]


# Exibir o menu
def exibir_menu():
    print("\n===== CATALOGO DE FILMES =====")
    print("1 - Cadastrar filme")
    print("2 - Listar filmes")
    print("3 - Buscar filme")
    print("4 - Remover filme")
    print("5 - Sair")


# Cadastrar filmes
def cadastrar(lista):
    print("\n===== CADASTRAR FILME =====")

    # Mostra os codigos que ja estao sendo usados
    print("\nCodigos ja cadastrados:")

    if len(lista) == 0:
        print("Nenhum codigo em uso.")
    else:
        for filme in lista:
            print(filme["codigo"], end=" | ")

    print("\n")

    try:
        codigo = int(input("Digite o codigo: "))

        if codigo <= 0:
            print("Codigo invalido!")
            return

    except ValueError:
        print("Codigo invalido!")
        return

    # Verifica se o codigo ja existe
    for filme in lista:
        if filme["codigo"] == codigo:
            print("Esse codigo ja esta cadastrado!")
            return

    titulo = input("Digite o titulo: ").strip()
    genero = input("Digite o genero: ").strip()

    if titulo == "" or genero == "":
        print("Titulo e genero nao podem ficar vazios!")
        return

    # Valida o ano
    try:
        ano = int(input("Digite o ano: "))

        if ano <= 0:
            print("Ano invalido!")
            return

    except ValueError:
        print("Digite um ano valido!")
        return

    # Valida a nota
    try:
        nota = float(input("Digite a nota (0 a 10): "))

        if nota < 0 or nota > 10:
            print("Nota invalida!")
            return

    except ValueError:
        print("Digite uma nota valida!")
        return

    # Cria o dicionario do novo filme
    novo_filme = {
        "codigo": codigo,
        "titulo": titulo,
        "genero": genero,
        "ano": ano,
        "nota": nota
    }

    # Adiciona o filme na lista
    lista.append(novo_filme)

    print("Filme cadastrado com sucesso!")


# Listar filmes
def listar(lista):
    print("\n===== LISTA DE FILMES =====")

    if len(lista) == 0:
        print("Nenhum filme cadastrado!")
        return

    for filme in lista:
        print("----------------------------")
        print("Codigo:", filme["codigo"])
        print("Titulo:", filme["titulo"])
        print("Genero:", filme["genero"])
        print("Ano:", filme["ano"])
        print("Nota:", filme["nota"])

    print("----------------------------")


# Buscar filmes
def buscar(lista):
    print("\n===== BUSCAR FILME =====")

    pesquisa = input("Digite o codigo ou parte do titulo: ").strip()

    if pesquisa == "":
        print("Digite alguma informacao para buscar!")
        return

    encontrado = False

    # Busca sequencial
    for filme in lista:

        if (str(filme["codigo"]) == pesquisa or
                pesquisa.lower() in filme["titulo"].lower()):

            print("\nFilme encontrado!")
            print("Codigo:", filme["codigo"])
            print("Titulo:", filme["titulo"])
            print("Genero:", filme["genero"])
            print("Ano:", filme["ano"])
            print("Nota:", filme["nota"])

            encontrado = True

    if encontrado == False:
        print("Filme nao encontrado!")


# Remover filmes
def remover(lista):
    print("\n===== REMOVER FILME =====")

    if len(lista) == 0:
        print("Nao existem filmes cadastrados!")
        return

    try:
        codigo = int(input("Digite o codigo do filme que deseja remover: "))

        if codigo <= 0:
            print("Codigo invalido!")
            return

    except ValueError:
        print("Codigo invalido!")
        return

    # Procura o filme pelo codigo
    for i in range(len(lista)):

        if lista[i]["codigo"] == codigo:

            removido = lista.pop(i)

            print("Filme removido com sucesso!")
            print("Filme:", removido["titulo"])
            return

    print("Filme nao encontrado!")


# Programa principal
while True:

    exibir_menu()

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        cadastrar(filmes)

    elif opcao == "2":
        listar(filmes)

    elif opcao == "3":
        buscar(filmes)

    elif opcao == "4":
        remover(filmes)

    elif opcao == "5":
        print("Programa encerrado. Ate mais!")
        break

    else:
        print("Opcao invalida! Tente novamente.")