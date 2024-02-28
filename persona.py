class persona:

    def __init__(self, nombre, anos):
        self.anos = anos
        self.nombre = nombre


    def imprimir(self):
        print("Nombre de la perosna: ", self.nombre, "Edad: ", self.anos)

    def cumpleanos(self):
        print("Cumple: ", self.anos + 1)


