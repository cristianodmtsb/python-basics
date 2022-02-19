"""
Formatando valores com modificadores

:s - Texto (string)
:d - inteiro (int)
:f - Numeros de ponto flutuante (float)
:.(NUMERO)f - quantidade de casas decimais
:(CARACTERE)(> ou < ou ^)(quantidade)(Tipo -s, d ou f

> - esquerda
< - direita
^ - Centro
"""
num1 = 10
num2 = 3
divisao = num1 / num2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

print(f'{num1:0>10}')
print(f'{num2:0>10}')
print(f'{num2:0<10}')
print(f'{num2:0^10}')
print(f'{num2:0>10.2f}')

nome = 'William Castro'
nome_formatado = '{:@>20}'.format(nome)
print(f'{nome_formatado}')
nome = nome.ljust(20, '#')
print(nome)
print(nome.lower())
print(nome.upper())
print(nome.title())