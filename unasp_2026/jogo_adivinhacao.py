numero_secreto = 7
tentativas = 0
palpite = 0

print("Tente descobrir o número entre 1 e 10.")

while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        print("Quantidade de tentativas:", tentativas)
    else:
        print("Você errou! Tente novamente.")