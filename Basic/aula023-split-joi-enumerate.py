""""
Split - dividir uma string
join - juntar uma lista de strings em uma única string
enumerate - retorna um objeto enumerate
"""

texto = 'Python é uma linguagem de programação Python'
lista = texto.split(' ')
lista2 = texto.split('m')

print(lista)
print(lista2)

for val in lista:
    print(f'{lista.count(val)} - {val}')

palavra = ''
contagem = 0
for valor in lista:
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra {palavra} apareceu {contagem} vezes')

# FUNÇÃO JOIN
lista3 = '-'.join(lista)
print(lista3)

# ENUMERATE
for i, valor in enumerate(lista):
    print(f'{i} - {valor}')