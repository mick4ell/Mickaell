contador = 0 
numero = int(input('Digite um numero(0 para parar): '))

while numero !=0:
    if numero % 2 == 0: 
        contador = contador + 1
    numero = int(input('Digite um numero(0 para parar): '))
print (f'Quntidade de numeros pares: {contador}')