def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"o Resutaldo da operação é = {resultado}")

exibir_resultado(30, 50, somar)
exibir_resultado(30, 50, subtrair)

op = somar

print(op(1, 3))