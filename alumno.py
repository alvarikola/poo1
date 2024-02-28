class alumno:

    def __init__(self):
        self.nota = 0
        self.nombre = ""


    def imprimir(self):
        print("Nombre del alumno: ", self.nombre, "nota del alumno: ", self.nota)

    def promociona(self):
        if (self.nota >= 5):
            print("El alumno", self.nombre, "promociona")
        else:
            print("No promociona")

def main():
    joel = alumno()
    joel.nombre = "joel"
    joel.nota = 7
    joel.imprimir()
    joel.promociona()


if __name__ == "__main__":
    main()