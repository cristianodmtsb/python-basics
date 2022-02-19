"""
Operadores Relacionais
== > >= < <= !=
"""

# print(2 == 2)  # True
# print(2 > 2)  # False
# print(2 >= 2)  # True
# print(2 < 2)  # False
# print(2 <= 2)  # True
# print(2 != 2)  # False

idade = input('Idade: ')
idade = int(idade)
idade_min = 20
idade_max = 30

if idade >= idade_min and idade <= idade_max:
    print('Emprestimo liberado')
else:
    print('Emprestimo nao pode')
