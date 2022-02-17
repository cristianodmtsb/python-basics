'''
Iniciar com letra, pode conter numeros, separar com _, letras minusculas
'''
nome = 'Cristiano'
idade = 35
altura = 1.75
e_maior = idade > 18
peso = 94
imc = peso / (altura ** 2)

print(nome, type(nome))
print('Nome:', nome)
print('Altura:', altura)
print('Idade:', idade)
print('De maior?:', e_maior)

print(idade * altura)

print(imc)