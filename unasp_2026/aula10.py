telefone = input("Digite o telefone no formato(xx)xxxxx-xxxx:  ")

ddd = telefone[1:3]
numero = telefone[4:]

print(f"DDD: {ddd}")
print(f"Número: {numero}")
print('')

data = input('Digite sua data de nacimento (DD/MM/AAAA): ')

dia = data[0:2]
mes = data[3:5]
ano = data[6:]

print(f'Dia: {dia}')
print(f'Mês: {mes}')
print(f'Ano: {ano}')

email = input('Digite seu email (nome.sobrenome@dominio.com): ')
nome = email[0:5]
dominio = email[6:15]
print(f'Nome: {nome}')
print(f'Dominio: {dominio}')