"""
Operadores lógicos
and, or, not
in, not in
"""
# verdadeiro E falso = falso
# comparacao1 and comparacao2

# verdadeiro e falso = verdadeiro
# comparacao1 or comparacao2

a = 2
b = 3

if not b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B')

nome = 'Cristiano'

if 's' in nome:
    print(f'Existe "S" em {nome}')


username = input('Username: ')
password = input('Password: ')

user_bd = 'cristiano'
pass_bd = '123456'

if user_bd == username and pass_bd == password:
    print(f'Bem vindo {nome}')
else:
    print('Usuario ou senha inválidos')