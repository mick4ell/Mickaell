consumo_total = 0
dias_alerta = 0

for dia in range(1, 8):
    consumo = float(input(f"Informe o consumo (kWh) do dia {dia}: "))
    consumo_total += consumo
    if consumo > 20:
        dias_alerta += 1

print("=" * 36)
print(f"Consumo total da semana: {consumo_total:.2f} kWh")
print(f"Dias com consumo acima de 20 kWh: {dias_alerta}")
print("=" * 36)
