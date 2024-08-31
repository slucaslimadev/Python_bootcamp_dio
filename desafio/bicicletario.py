class bicicletario:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def buzinar(self):
        print("BIBIBI ...")
    def parar(self):
        print("PARANDO ...")
    def correr(self):
        print("CORRENDO ...")

bike_1 = bicicletario("Azul", "10ZINHA", "2013", 10000)
bike_1.buzinar()
print(bike_1.valor)