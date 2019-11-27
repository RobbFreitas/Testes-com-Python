compra = float(input('Informe valor da compra: '))
desc = float(input('Informe valor do desconto: '))
val_pago = float(input('Informe valor pago: '))
desc1 = (desc*val_pago)/100
pago_desc = val_pago - desc1
troco = val_pago - pago_desc
print('o pago foi {} e o desconto foi de {} e o troco {}'.format(pago_desc, desc1, troco)) 
