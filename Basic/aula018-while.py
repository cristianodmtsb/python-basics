"""
while
utilizado para realizar açoes enquanto
uma condiçao for verdadeira
"""
x = 0
y = 0

# while x < 10:
#     if x == 3:
#         x = x + 1
#         continue #continua a partir dessa condiçao
#
#     print(x)
#     x = x + 1
#
# print('It is over')

# while x < 10:
#     if x == 3:
#         x = x + 1
#         break #para a partir dessa condiçao
#
#     print(x)
#     x += 1
#
# print('It is over 3')

# while x < 5:
#     y = 0
#
#     while y < 5:
#         print(f'({x},{y})')
#         y += 1
#     x += 1
#
# print('acabou')

while True:
    print()
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operador = input('Digite operador ou SAIR: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Voce precisa digitar um numero ou SAIR para finalizar')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == 'SAIR':
        break