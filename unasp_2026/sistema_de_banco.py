#inicio
nome = 'mickaell'
print('----------Banco---------')
menu = int(input('Digite 1, Para ver o saldo. 2, para realizar um deposito. 3, para realizar saque: '))
saldo = 500.00

#processamento
if menu == 1:
    print(f'nome: mickaell\nSaldo R${saldo}')

elif menu == 2:
    deposito = float(input("Digite o valor do depósito: R$ "))
    saldoo = saldo + deposito
    print(f"Depósito realizado com sucesso!\nNovo saldo: R$ {saldoo:.2f}")

elif menu == 3:
    saque = float(input("Digite o valor do saque: R$ "))
    saldo_agora = saldo - saque

    if saque > 0 and saque <= saldo:
        print("Saque realizado com sucesso!")
        print(f"Novo saldo: R$ {saldo_agora:.2f}")
    else:
        print('Valor Inválido!')

else:
    print('opição invalida') 
