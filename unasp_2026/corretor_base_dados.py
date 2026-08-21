bruto = [
    " MARIA DA SILVA ",
    "joap@email.com ",
    "  RUA DAS FLORES, NO 123  ",
    " 000.111.222-33  ",
    " CARLOS.ROCHA@ESCOLA.COM ",
    " AV.CENTRAL, No 450 "
]

dados_limpos = []

for dado in bruto:
    texto = dado.strip()
    if "@" in texto:
        texto = texto.lower()
    else:
        texto = texto.replace("No", "Numero")
        texto = texto.replace(".", "").replace("-", "")

    dados_limpos.append(texto)

print("="*36)
print('         BASE DE DADOS TRATADA E SANITIZADA         ')
print("="*36)

for dado in dados_limpos:
    print(f"- {dado}")
