valor = float(input('Digite o valor total da compra  R$ '))
cliente = input('o cliente é assinante prime? (sim/nao): ').lower()
pagamento = input('forma de  pagamento (dinheiro/cartao): ').lower()
cupom = input('A compra usa cupom de liquidação externa (sim/nao) ').lower()

if  cupom == 'sim':
    desconto = 0
    motivo = 'cupom externo ativo'
else:
    if valor >= 200 and cliente == 'sim':
        desconto = 20
        motivo = 'Criterio prime + valor atingindo'
    elif valor >= 150.0 or pagamento == ' dinheiro':
        desconto = 10
        motivo = ' criterio de incetivo atigindo'
    else:
        desconto = 0
        motivo = 'nenhum criterio atingido'

desconto = valor * (desconto/100)
total = valor - desconto
print(f'Desconto aplicado: {desconto}% {motivo}\nTotal a pagar: R${total:.2f}')