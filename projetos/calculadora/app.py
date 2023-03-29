import os
import sys
sys.path.insert(0, os.getcwd())
from projetos.calculadora import calcule




op = input('Entre com a operação a ser realizada ( + | - | * | / ): ')
a = float(input(f'Entre com o valor de a na operação a{op}b: '))
b = float(input(f'Entre com o valor de b na operação a{op}b: '))
print(f"{a}{op}{b}={calcule(op,a,b)}")