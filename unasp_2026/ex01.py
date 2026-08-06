total_compra = 0
quantidade_itens  = int(input('quantidade de itens: '))

for i in range(1, quantidade_itens + 1):
    preco = float(input(f'preço do item {i}: '))
    total_compra += preco 

media = total_compra / quantidade_itens

print("=" * 36)
print(f"Total da compra: R$ {total_compra:.2f}")
print(f"Média de preço por item: R$ {media:.2f}")
print("=" * 36)