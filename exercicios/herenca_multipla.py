class Animal:
    def __init__(self, nro_patas):
        self.nrmo_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass
class Gato(Mamifero):
    pass
class Leao(Mamifero):
    pass

class Onitorrinco(Mamifero, Ave):
    pass

# gato1 = Gato(4, "Cinza")
# print(gato1)    
oni1 = Onitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="Preto")
print(oni1)

