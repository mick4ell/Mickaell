senha_correta = "incorreta"
tentativa = input("Digite a senha: ")

while tentativa != senha_correta:
    print("Senha Incorreta! Tente Novamente")
    tentativa = input("Digite a senha: ")
print("Senha Correta")