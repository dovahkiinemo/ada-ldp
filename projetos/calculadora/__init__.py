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
    


