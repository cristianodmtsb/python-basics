idade = input('Digite sua idade: ')

if not idade.isdigit():
    print('Idade inválida - digite um numero')
else:
    idade = int(idade)
    de_maior = idade >= 18
    msg = 'de maior' if de_maior else 'menor'

    print(f'Você é {msg} de idade')