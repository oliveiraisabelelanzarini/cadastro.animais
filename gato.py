from animal import Animal
class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca = raca
    def getRaca(self):
        return self.__raca
    def setRaca(self, raca):
        self.__raca = raca
    
    def mostrar(self):
        return (f"nome: {self.getNome()}, idade: {self.getIdade()}, raca: {self.getRaca()}")
    
g = Gato("Miau", 4, "Sianês")
print(g.mostrar())