class OrdenadorNumeros:
    def __init__(self, num1, num2, num3):
        self.numeros = [num1, num2, num3]

    def ordenar(self):
        self.numeros.sort()

    def mostrar(self):
        print("Los números en orden ascendente son:", self.numeros)


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

ordenador = OrdenadorNumeros(num1, num2, num3)

ordenador.ordenar()
ordenador.mostrar()
