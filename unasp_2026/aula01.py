print('ola mundo')

nome = input("Digite seu nome: ")
print("ola",nome)

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2 ) /2
print("media:", media)

frequencia = float(input("Digite a frequencia: "))

print("media >=6 ",media>=6)
print("frequencia >=75 ",frequencia>=75)
print("aprovado:", (media>=6) and (frequencia>=75))