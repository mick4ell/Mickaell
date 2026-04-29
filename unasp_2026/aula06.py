destino = input('Digite o seu nome do seu destino: ')
dinheiro = float(input('quanto vc tem ter para ira para la R$'))
dolar = float(input('quanto esta a cotação atual do dólar (USE PONTO NO LUGAR DA VIRGULA): '))
cal = dinheiro / dolar
print (f'a sua viagem para {destino} vai custar USS${cal:.2f}')