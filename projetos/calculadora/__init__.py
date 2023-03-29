from funcoes import soma,subtracao,multiplicacao,divisao

def calcule(opcao,a,b):
    if opcao == '+':
        return soma(a,b)
    elif opcao == '-':
        return subtracao(a,b)
    elif opcao == '*':
        return multiplicacao(a,b)
    elif opcao == '/':
        return divisao(a,b)
    else:
        print("Operação inválida")
        return 0
    
op = input('Entre com a operação a ser realizada ( + | - | * | / ): ')
a = float(input(f'Entre com o valor de a na operação a{op}b: '))
b = float(input(f'Entre com o valor de b na operação a{op}b: '))
print(f"{a}{op}{b}={calcule(op,a,b)}")

