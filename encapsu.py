class Encapsulamento:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é private'
    
    def metodo_publico(self):
        print(self.__exemplo)
        return 'Método Público'
    
    def _metodo_protegido(self):
        return 'Método Protegido'
    
    def __metodo_private(self):
        return 'Método Private'

enca = Encapsulamento()
print(enca.public)
print(enca.metodo_publico())
print(enca._protected)
print(enca._metodo_protegido())
print(enca.__exemplo)
print(enca.__metodo_private())