nome = input( 'Qual é o seu nome? ')

if nome:
    print( 'Prazer em te conhecer {:s}'.format( nome ) )
else:
    print('Cade seu nome?')

print(nome or 'Cade seu nome?')