def soma(x,y):
    try:
        return x + y
    except TypeError:
        print(f"O input 'a' e 'b' devem ser um int/float, recebido {a}, {type(a)}, e {b},  {type(b)}")

def subtracao(x,y):
    try:
        return x - y
    except TypeError:
        print(f"O input 'a' e 'b' devem ser um int/float, recebido {a}, {type(a)}, e {b},  {type(b)}")

def multiplicacao(x,y):
    try:
        return x * y
    except TypeError:
        print(f"O input 'a' e 'b' devem ser um int/float, recebido {a}, {type(a)}, e {b},  {type(b)}")

def divisao(x,y):
    if y == 0:
        print("Divisão inválida, denominador igual a zero.")
        return 0
    else:
        return x/y