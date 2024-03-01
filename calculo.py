class Calculo:
    
    def __init__(self, numero1:int, numero2:int):
        self.numero1 = numero1
        self.numero2 = numero2

    
    def suma(self):
        print(self.numero1 + self.numero2)


    def resta(self):
        print(self.numero1 - self.numero2)


    def multiplicacion(self):
        print(self.numero1 * self.numero2)


    def division(self):
        print(self.numero1 / self.numero2)



if __name__ == "__main__":
    operacion = Calculo(1, 2)
    operacion.suma()
    operacion.resta()
    operacion.multiplicacion()
    operacion.division()