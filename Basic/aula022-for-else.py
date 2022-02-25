"""
For / Else
"""

lista = ['aJoao', 'Maria', 'Pedro', 'Joana']

for elemento in lista:
    print(elemento)
    if elemento.startswith('J'):
        print(elemento)
        break
else:
    print('Nenhum elemento começa com J')