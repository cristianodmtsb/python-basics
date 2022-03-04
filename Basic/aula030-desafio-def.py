"""
1 - Crie uma função que exibe uma saudação com os parametros saudação e nome.
"""
def hello(saudacao, nome):
    print(saudacao, nome)

hello('Olá', 'João')
"""
2 - crie uma função que receba 3 numeros e retorne a soma dos 3 numeros.
"""
def soma(a, b, c):
    print( a + b + c)

soma(1, 2, 3)
"""
3 - Crie uma função que receba 2 numeros. O primiero é um valor e o segundo o percentual. Retorne o valor do percentual do primeiro valor.
"""
def percentual(valor, percentual):
    print(valor + ( valor * percentual )/ 100)

percentual(100, 10)
percentual(225, 20)
"""
4 - Fizz Buzz - Faça um programa que imprima todos os números entre 1 e 100. Mas, para múltiplos de 3 imprima “Fizz”. Para múltiplos de 5 imprima “Buzz”. Para números múltiplos de 3 e 5 imprima “FizzBuzz”.
"""
def fizzbuzz(num):
    # for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

fizzbuzz(15)
