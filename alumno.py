class alumno:

    def __init__(self, nombre, nota):
        self.nota = nota
        self.nombre = nombre


    def imprimir(self):
        print("Nombre del alumno: ", self.nombre, "nota del alumno: ", self.nota)

    def promociona(self):
        if (self.nota >= 5):
            print("El alumno", self.nombre, "promociona")
        else:
            print("No promociona")

def main():
   pass


if __name__ == "__main__":
    main()