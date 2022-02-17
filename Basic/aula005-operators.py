'''
+, -, *, /. //, **, %, ()
'''

print(10 + 10)  # Adiçao
print(10 - 10)  # Subtraçao
print(10 * 10)  # Multiplicaçao
print(10 / 3)  # Divisao = 3.3333333333333335

print(10 // 3)  # 3.0
print(10 ** 3)  # 1000
print(10 % 3)  # 1
print(5+2*10)  # 25
print((5+2)*10)  # 70
print(5*'A')  # AAAAA

'''
Precedência dos Operadores Aritméticos
Assim como aprendemos na matemática, operadores têm uma certa precedência que pode ser alterada 
usando os parênteses (como descrito na aula anterior).

Abaixo, segue uma lista mais precisa de quais operadores tem maior prioridade na hora de 
realizar contas mais complexas (de maior para menor precedência).

( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

** - Depois vem a exponenciação

* / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

+  - - Por fim, soma e subtração

Contas com operadores de mesma precedência são realizadas da esquerda para a direita.

Observação: existem muito mais operadores do que estes em Python e todos eles também têm 
precedência, você pode ver a lista completa em 
https://docs.python.org/3/reference/expressions.html#operator-precedence (sempre utilize a 
documentação oficial como reforço caso necessário).

Caso tenha dúvidas, faça testes com números. Por exemplo, olhe para essa conta e tente decifrar 
como chegar no resultado: 2 + 5 * 3 ** 2 - (23.5 + 23.5) (o resultado é 0.0). Para isso você 
precisa realizar as contas com maior precedência primeiro.
'''
