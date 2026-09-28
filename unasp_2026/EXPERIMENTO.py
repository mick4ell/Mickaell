def criar_usuario():
    nome_usuario = "Dev_Python"
    nivel_acesso = "Admin"
    print("--- DENTRO DA FUNÇÃO ---")
    print(f"Usuário criado: {nome_usuario} ({nivel_acesso})")
    return nome_usuario

usuario = criar_usuario()

print("--- FORA DA FUNÇÃO ---")
print(usuario)

def contagem_regressiva(n):
    print(f"Entrando no nível: {n}")
    if n == 0:
        print("DECOLAR! (Caso Base Atingido)")
    else:
        contagem_regressiva(n - 1)
    print(f"Saindo do nível: {n}")

contagem_regressiva(3)

import sys
print("Limite:", sys.getrecursionlimit())

def funcao_infinita(contador):
    print(f"Chamada número: {contador}")
    funcao_infinita(contador + 1)

funcao_infinita(1)

def soma_ate(n):
    if n <= 1:
        return 1
    else:
        return n + soma_ate(n - 1)

resultado = soma_ate(5)
print(f"A soma acumulada é: {resultado}")