# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...


c1 = Cliente('Luiz', 'Otávio')

# print(c1.nome, c1.sobrenome)
c1.falar_nome_classe()

a1 = Aluno('Maria', 'Helena')

# print(a1.nome, a1.sobrenome)
a1.falar_nome_classe()