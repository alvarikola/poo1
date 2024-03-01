class Calculo:
    
    def __init__(self, numero1:int, numero2:int):
        self.numero1 = numero1
        self.numero2 = numero2

    
    def suma(self):
        self.sum = self.numero1 + self.numero2
        print(f"El resultado de la suma es: {self.sum}")


    def resta(self):
        self.rest = self.numero1 - self.numero2
        print(f"El resultado de la resta es: {self.rest}")


    def multiplicacion(self):
        self.multi = self.numero1 * self.numero2
        print(f"El resultado de la multiplicación es: {self.multi}")


    def division(self):
        self.divi = self.numero1 / self.numero2
        print(f"El resultado de la división es: {self.divi}")



if __name__ == "__main__":
    operacion = Calculo(1, 2)
    operacion.suma()
    operacion.resta()
    operacion.multiplicacion()
    operacion.division()