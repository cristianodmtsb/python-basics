"""
While/Else
contadores
acumuladores
"""

count = 1
acumulador = 1

while count <= 10:
    print(count, acumulador)

    acumulador += count
    count += 1
else:
    print('Final else')

# WHILE strings
# indice 0123456789012345678901234567890123
frase = 'o rato roeu a roupa do rei de roma'
size = len(frase)
contador = 0
nova_string = ''

while contador < size:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    contador += 1

print(nova_string)