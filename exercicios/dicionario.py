dados = {"cliente1": {"nome": "Lucas", "idade": 24},
         "cliente2": {"nome": "Yasmin", "idade": 20}}

print(dados.items())
print(dados.get("cliente1", {"NÃO EXISTE"}))