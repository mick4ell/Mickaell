# progama_de_mercado
nome = input("Qual é o nome do cliente: ")
valor = float(input('Qual é o valor do produto: '))
quantidade = int(input('Qual é a quantidade comprada: '))

total = valor * quantidade
desco = total * 0.10
condicao = total >= 100
com_desco = total - desco

print(f"Cliente: {nome}")
print(f"Valor total: R$ {valor:.2f}")
print(f"Desconto: R$ {desco:.2f}")
print(f"Total a pagar: R$ {com_desco:.2f}")
print(f'tem direito ao desconto? {condicao:.2f}')