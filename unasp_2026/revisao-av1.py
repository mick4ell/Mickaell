def formatar_citacao(nome_completo):
    partes = nome_completo.strip().split()
    sobrenome = partes[-1].upper()
    nomes_restantes = " ".join(partes[:-1])
    return sobrenome + ", " + nomes_restantes

resultado = formatar_citacao("Carlos Eduardo Andrade")
print(resultado) 

def gerar_codigo(ano, cpf):
    cpf_limpo = cpf.strip()
    primeiros_digitos = cpf_limpo[0:3]
    return "ALU-" + str(ano) + "-" + primeiros_digitos

resultado2 = gerar_codigo("2026", "123.456.789-00")
print(resultado2)