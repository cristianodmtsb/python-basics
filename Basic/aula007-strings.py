'''
Strings
'''

nome = 'Cristiano'
idade = 35
altura = 1.75
e_maior = idade > 18
peso = 94
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos e seu imc é {imc:.2f}')
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {ic:.2f}'.format(n=nome, i=idade, ic=imc))