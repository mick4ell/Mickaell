num = int(input("Digite um número de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o numero {}'.format(num))
print('unidade: {}'.format(u))
print('denzena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))