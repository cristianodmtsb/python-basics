"""
For in
Iterando strings com for
Funçao range (start=0, stop, step=1)
"""
frase = 'o rato'
nova_frase = ''

for letra in frase:
    print(letra)

# imprime a letra R maiuscula
for letra in frase:
    if letra == 'r':
        nova_frase += letra.upper()
    else:
        nova_frase += letra
print(nova_frase)

# FOR ENUMERADO
for i, letra in enumerate(frase):
    print(i, letra)

# RANGE CRESCENTE
for numero in range(10):
    print(numero)

# RANGE DECRECESTE
for numero in range(20, 10, -1):
    print(numero)

# INICIA EM 0 E VAI ATE 10 de 2 em 2
for numero in range(0, 10, 2):
    print(numero)

# MULTIPLOs o mesmo do de cima
for n in range(100):
    if n % 8 == 0:
        print(n)