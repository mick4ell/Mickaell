nome = input('Digite o seu nome: ')
nivel_acesso = int(input('Qual é o seu nivel de Privilégio: '))
chave_ativa = input('Você tem a chave de criptografia: ')

perm = acesso_permitido = (nivel_acesso >= 3) and chave_ativa == True

print(f'Verificando segurança para: {nome}')
print(f'Acesso autorizado: {perm}')