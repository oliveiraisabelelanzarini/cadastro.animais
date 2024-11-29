from animal import Animal
class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__porte = porte
    
    def getPorte(self):
        return self.__porte
    def setPorte(self, porte):
        self.__porte = porte 
    
    def mostrar(self):
        return (f"nome: {self.getNome()}, idade: {self.getIdade()}, porte: {self.getPorte()}")
    
c = Cachorro("Rex", 3, "Grande")
print(c.mostrar())