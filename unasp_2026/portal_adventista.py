nome = input('Digite o seu nome: ')
uni = input('Voce esta com o uniforme completo (responder com "sim" ou "nao"): ')
if uni == 'sim':
    print(f" Bem-vindo, {nome}! Siga para o pátio para o culto.")
else:
     print(f" {nome}, por favor, dirija-se à Coordenação antes da aula.")
hora = int(input('Que goras são. (use um número inteiro): '))
if hora <= 7:
    print(' "Bom dia! Você chegou no horário."')
else:
    print("Você está atrasado. Por favor, retire sua autorização na secretaria.")