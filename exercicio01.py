#QUESTÃO 1
def relactions():
    n1 = int(input('Primeiro Numero: '))
    n2 = int(input('Segundo Numero: '))

    print(f'O valor da avaliação da expressão {n1} > {n2} , é {n1 > n2} ')
    print(f'O valor da avaliação da expressão {n1} < {n2} é {n1 < n2} ')
    print(f'O valor da avaliação da expressão {n1} == {n2} , é {n1 == n2} ')
    print(f'O valor da avaliação da expressão {n1} >= {n2} , é {n1 >= n2} ')
    print(f'O valor da avaliação da expressão {n1} <= {n2} , é {n1 <= n2} ')
# QUESTÃO 2
def stringrelactions():
    s1 = input('Digite algo: ')
    s2 = input('Digite algo²')

    print(f"O valor da avaliação da expressão {s1} > {s2}, é {len(s1) > len(s2)}")
    print(f"O valor da avaliação da expressão {s1} < {s2}, é {len(s1) < len(s2)}")
    print(f"O valor da avaliação da expressão {s1} == {s2}, é {len(s1) == len(s2)}")
    print(f"O valor da avaliação da expressão {s1} >= {s2}, é {len(s1) >= len(s2)}")
    print(f"O valor da avaliação da expressão {s1} <= {s2}, é {len(s1) <= len(s2)}")

# QUESTÃO 3 (ai está a tabela completada.)
def TrueTable():
    print("""
    | False and False = False |
    | False and True = False  |
    | True and False = False  |
    | True and True = True    |
    """)
# QUESTÃO 4

def printable():
    print("O resultado da operação False and False é:", False and False)
    print("O resultado da operação False and True é:", False and True)
    print("O resultado da operação True and False é:", True and False)
    print("O resultado da operação True and True é:", True and True)

# QUESTÃO 5 (ai está a tabela completada.)
def printor():
    
    print("""| False or False = False |
| False or True | True   |
| True or False | True   |
| True or True  | True   |""")
# QUESTÃO 6
def orprint():
    print("O resultado da operação False or False é: ",False or False)
    print("O resultado da operação False or True é:", False or True)
    print("O resultado da operação True or False é:", True or False)
    print("O resultado da operação True or True é:", True or True)

# QUESTÃO 7 (ai está a tabela completada.)
def notprint():
    print("""
    VALOR, RESULTADO DO NOT
    False | True
    True  | False """)

# QUESTÃO 8
def notresult():
    print("O valor da operação not False é:",not False)
    print("O Valor da operação not True é:",not True)

# QUESTÃO 9
def questao9():
    print("""w = x * y < z/x or x/y > z * x and y < x
w = x * y < z / x or x / y > z * x and z * y < x
w = 10 * -2 < 5 / 10 or 10 / -2 > 5 / 10 and 5 * -2 < 10
w = -20 < 5 / 10 or 10 / -2 > 5 / 10 and 5 * -2 < 10
w = -20 < 0.5 or 10 / -2 > 5 / 10 and 5 * -2 < 10
w = -20 < 0.5 or -5 > 5 / 10 and 5 * -2 < 10
w = -20 < 0.5 or -5 > 5 / 10 and 5 * -2 < 10
w = -20 < 0.5 or -5 > 0.5 and 5 * -2 < 10
w = -20 < 0.5 or -5 > 0.5 and -10 < 10
w = True or -5 > 0.5 and -10 < 10
w = True or False and -10 < 10
w = True or False and True
w = True or False
w = True """)
# QUESTÃO 10
def wresult():
    x = int(input('Digite um valor para X: '))
    y = int(input("Digite um valor para y: "))
    z = int(input("Digite um valor para Z: "))
    w = x * y < z/x or x/y > z * x and y < x
    print(w)


relactions()
stringrelactions()
TrueTable()
printable()
printor()
orprint()
notprint()
notresult()
questao9()
wresult()
