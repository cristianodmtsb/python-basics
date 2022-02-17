'''
- Criar variaveis para nome (str), idade (int)
- altura (float) e peso (float) de uma pessoa
- criar variavel com o ano atual (int)
- obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
- obter o imc da pessoa com 2casas decimais (peso e na aultra da pessoa)
- exibir um testo com todos os valores na tela usando o F-strings (com as chaves)
'''

nome = 'Cristiano'
idade = 35
altura = 1.75
peso = 94
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / (altura ** 2)  # altura ao quadrado

print(f'{nome} tem {idade} anos, {altura} de altura e seu peso {peso}kg')
print(f'O IMC do {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')
