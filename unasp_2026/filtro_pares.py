limite = int(input("Digite um número limite: "))
print(f"Números pares de 0 até {limite}: ")

for numero in range(0, limite + 1):
    if numero % 2 == 0:
        print(numero)