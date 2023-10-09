class Caneta:
    def __init__(self, cor, tampa=None):
        self.cor = cor
        self.cor_tampa = tampa

    @property
    def cor(self):
        print("Getter")
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print("Setter")
        self._cor = valor
    
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, tampa):
        self._cor_tampa = tampa


caneta = Caneta('Azul', 'Verde')
print(caneta.cor_tampa)
caneta.cor_tampa='Branco'
print(caneta.cor_tampa)