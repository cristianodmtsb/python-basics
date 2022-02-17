'''
Tipos de dados
str - string
int - inteiro
float - flutuante
bool - boolean
'''

print('Cris', type('Cris'))
print(35, type(35))
print(35.6, type(35.6))
print(10 == 10, type(10 == 10))
# print(bool(''))

# Type casting
print(type('Cris'), bool('Cris'))  # <class 'str'> True
print(type('10'), type(int('10')))  # <class 'str'> <class 'int'>
print(type(10), type(str(10)))  # <class 'int'> <class 'str'>
print(type('10.2'), type(float('10.2')))  # <class 'str'> <class 'float'>
