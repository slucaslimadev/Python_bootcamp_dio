def analise_vendas(numeros):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(numeros)
    media_vendas = total_vendas / len(numeros)
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:

    lista_entrada = list(map(int, entrada.split(',')))

    return lista_entrada

numeros = obter_entrada_vendas()
print(analise_vendas(numeros))
