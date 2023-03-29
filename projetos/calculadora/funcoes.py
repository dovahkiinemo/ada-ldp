def soma(x,y):
    try:
        return x + y
    except TypeError:
        print(f"O input 'a' e 'b' devem ser um int/float, recebido {x}, {type(x)}, e {y},  {type(y)}")

def subtracao(x,y):
    try:
        return x - y
    except TypeError:
        print(f"O input 'a' e 'b' devem ser um int/float, recebido {x}, {type(x)}, e {y},  {type(y)}")

def multiplicacao(x,y):
    try:
        return x * y
    except TypeError:
        print(f"O input 'a' e 'b' devem ser um int/float, recebido {x}, {type(x)}, e {y},  {type(y)}")

def divisao(x,y):
    if y == 0:
        print("Divisão inválida, denominador igual a zero.")
        return 0
    else:
        return x/y