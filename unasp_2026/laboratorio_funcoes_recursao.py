TAXA_PROCESSAMENTO = 2.00


def calcular_frete(valor_compra, peso_kg):
    taxa_base_frete = peso_kg * 5
    frete_final = taxa_base_frete

    if valor_compra >= 200:
        frete_final = frete_final * 0.5

    return frete_final


def aplicar_cupom(valor_item, cupom_desconto):
    valor_desconto = valor_item * (cupom_desconto / 100)
    valor_com_desconto = valor_item - valor_desconto
    preco_final = valor_com_desconto + TAXA_PROCESSAMENTO

    return preco_final


def exibir_cronograma_regressivo(parcelas_restantes, valor_parcela):
    if parcelas_restantes == 0:
        print("Todas as parcelas foram quitadas!")
        return

    print(f"Restam {parcelas_restantes} parcela(s) de R$ {valor_parcela}")
    exibir_cronograma_regressivo(parcelas_restantes - 1, valor_parcela)


while True:
    print("\n===== MÓDULO FINANCEIRO E LOGÍSTICO DA LOJA VIRTUAL =====")
    print("1 - Calcular Frete")
    print("2 - Aplicar Cupom de Desconto")
    print("3 - Ver Cronograma de Parcelas")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor_compra = float(input("Digite o valor da compra: "))
        peso_kg = float(input("Digite o peso da encomenda em kg: "))
        resultado_frete = calcular_frete(valor_compra, peso_kg)
        print(f"Frete Final: {resultado_frete}")

    elif opcao == "2":
        valor_item = float(input("Digite o valor do item: "))
        cupom_desconto = float(input("Digite o percentual de desconto do cupom: "))
        resultado_cupom = aplicar_cupom(valor_item, cupom_desconto)
        print(f"Preço Final: {resultado_cupom}")

    elif opcao == "3":
        parcelas_restantes = int(input("Digite o número de parcelas: "))
        valor_parcela = float(input("Digite o valor de cada parcela: "))
        exibir_cronograma_regressivo(parcelas_restantes, valor_parcela)

    elif opcao == "4":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")