"""
Listas
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E']
#         4    3    2    1    0
nova_lista = ['G', 'F', 'H', 'I', 'J', 'W']
lista3 = list(range(0,100,8))

# mostrando valor unico
print(lista[2])

"""
alterando valor
lista[4] = 'Outro texto'
print(lista)
"""
# mostrando apenas alguns itens
print(lista[2:4])
print(lista[:4])
print(lista[2:])
print(lista[-1])
print(lista[::2])
print(lista[::-1])

# APPEND
print(lista + nova_lista)
nova_lista.append(lista)
print(nova_lista)

# INSERT
nova_lista.insert(0, 'Banana')
print(nova_lista)

# POP
nova_lista.pop() #slimina o ultimo elemento
print(nova_lista)

# DEL
del(nova_lista[2:3])
print(nova_lista)
del(nova_lista[0])
print(nova_lista)

# MIN MAX
print(min(nova_lista))
print(max(nova_lista))

# LISTANDO
print(lista3)

# type check
lista4 = ['String', True, 10, -10.5]
for elment in lista4:
    print(type(elment))




