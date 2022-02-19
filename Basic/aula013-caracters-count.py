username = input('Username: ')
qtd_caracters = len(username)

print(username, qtd_caracters, type(qtd_caracters))

if qtd_caracters < 6:
    print('Pelo menos 6 caracteres')