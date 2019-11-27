op = 's'
while op != 'n':
    real = float(input('Entre com a quantia em reais: '))
    print('Digite E para Euro ou D para Dólar')
    moeda = str(input('Digite a moeda: '))
    if moeda == 'e' or 'E':
        print(real * 3.0)
    elif moeda == 'd' or 'D':
        print(real * 4.30)
    else:
        print('Erro! moeda não identificada')

    op = str(input('Deseja fazer outra operação? digite: s para continuar ou n para parar: '))

