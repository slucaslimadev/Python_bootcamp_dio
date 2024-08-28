Nome = "Lucas"
Amor = "Yasmin"
saldo = 10.23213
dados = {"nome": "Lucas", "idade": 24.333}

print("Nome: %s Amor: %s" % (Nome, Amor)) 
print("Nome: {} Amor: {}".format(Nome, Amor))
print("Nome: {1} Amor: {0}".format(Nome, Amor))
print("Nome: {nome} Amor: {amor}".format(nome=Nome, amor=Amor))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {Nome} Amor: {Amor}")
print(f"Nome: {Nome}, Saldo: {saldo:20.3f}")
print(f"Nome: {Nome}, Saldo: {saldo:.1f}")