nome = input("nome do atleta ")
peso = float(input("peso do atleta(kg): "))
exame = input("exame medico em dia?(sim/nao): ").lower()

if exame == "sim":
    if peso <60:
        categoria = "pena"
    elif peso >= 60 and peso <=80:
        categoria = "medio"
    else:
        categoria = "pesado"
    print(f"inscriçao confirmada!")
    print(f"atleta:{nome} | {categoria}")
else:
    print(f" inscriçao negada!")
    print(f"motivo: o atleta {nome} prescisa do exame medico")
