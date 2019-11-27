def soma (a,b):
    return(a+b)
def sub (a,b):
    return (a-b)
def multi (a,b):
    return (a*b)
def divi (a,b):
    return (a/b)

num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))

print('Opções:\n 1-Soma\n 2-Subtração\n 3-Multiplicação\n 4-Divisão\n 5- 0 para parar')
op = 1
while 0 <= op <= 4:
    op = int(input('Qual operação deseja fazer: '))
    if op == 1:
        print(soma(num1,num2))
    elif op == 2:
        print(sub(num1,num2))
    elif op == 3:
        print(multi(num1,num2))
    elif op == 4:
        print(divi(num1,num2))
    elif op == 0:
        break
    else:
        print('operação desconhecida')