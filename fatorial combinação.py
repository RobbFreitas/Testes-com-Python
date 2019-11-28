from math import factorial
n = float(input('Ente com o valor de n: '))
p = float(input('Entre com o valor de p: '))
print('A fórmula é C(n,p) = n!/p!*(n-p)!')
oper = factorial(n) / (factorial(p) * factorial((n - p)))

print(oper)