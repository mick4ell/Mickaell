print('Olá mundo')

num = input('Digite um número ')
print('Seu número é {}'.format(num))

num = int(input('Primeiro número '))
num2 = int(input('Segundo número '))
soma = num + num2
print('A soma entre os dois números é {}'.format(soma))

b1 = float(input('Bimestre um '))
b2 = float(input('Bimestre dois '))
b3 = float(input('Bimestre três '))
b4 = float(input('Bimestre quatro '))
soma = b1 + b2 + b3 + b4
print('A média bimestral é {:.2f}'.format(soma))

m = float(input('Metros '))
cm = m / 100
print('Convertido em centímetros fica {:.2f}'.format(cm))

qua = float(input('Qual os lado do quadrado '))
area = (qua * qua)
area2 = (qua * qua) * 2
print('A área é {:.2f}, o dobro é {:.2f}'.format(area, area2))