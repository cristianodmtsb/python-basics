# JOGO DA FORCA
secret = 'palavra'
digitados = []
chances = 3

while True:
    if chances <= 0:
        print('Perdeu sacaninha')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Volta, só uma letra')
        continue

    digitados.append(letra)

    if letra in secret:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Aff: a "{letra}" NAO EXISTE na palavra secreta')
        chances -= 1
        digitados.pop()

    secret_temp = ''
    for letra_secret in secret:
        if letra_secret in digitados:
            secret_temp += letra_secret
        else:
            secret_temp += '*'

    if secret_temp == secret:
        print('Parabens voce ganhou!')
        print(f'A palavra secreta é: {secret}')
        break
    else:
        print(f'Voce tem: {chances} chances')
        print(f'Ta quase olha aqui: {secret_temp}')
print()

