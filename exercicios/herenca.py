class veiculos:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    def ligar(self):
        print('Ligando ...')

class moto(veiculos):
    pass
class caminhao(veiculos):
    pass
class carro(veiculos):
    pass

carro1 = carro("Preto", "ABC-1234", 4)
carro1.ligar()

moto1 = moto("Branco", "DEF-1234", 2)
moto1.ligar()

caminhao1 = caminhao("Lilas", "HIJ-443", 4)
caminhao1.ligar()