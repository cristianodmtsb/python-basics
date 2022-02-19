"""
Faça um programa que recebe um número inteiro
informe se esta número é par ou impar
Caso nao seja um numero informe o erro
"""
num = input('Digite um numero: ')

if num.isdigit():
    num = int(num)
    num_type = num % 2
    if num_type == 0:
        print('Numero par')
    else:
        print('Numero impar')
else:
    print('Digite um numero')


"""
Faça um programa que pergunte a hora ao usuario
Exiba a saudaçao apropriada. Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
hora = input('Que horas sao?: ')

if not hora.isdigit():
    print('Digite uma hora')
else:
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora > 11 and hora <= 17:
        print('Boa tarde')
    else:
        print('Boa noite')


"""
Faça um programa que pede o Primeiro nome do usuario. 
Se o nome tiver 4 letras ou menos informe nome curto, se tiver entre 5 e 6 informe nome normal
maios que 6 letras informe nome grande
"""
nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Nome curto')
elif tamanho <= 6:
    print('Nome normal')
else:
    print('Nome grande')