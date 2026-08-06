valor_total = float(input('Digite o valor total da compra: '))

print("=" * 36)
print(f"TABELA DE PARCELAMENTO - COMPRA R$ {valor_total:.2f}")
print("=" * 36)

for parcela in range(1, 11):
    valor_parcela = valor_total / parcela
    print(f"{parcela}x de R$ {valor_parcela:.2f}")

print("=" * 36)