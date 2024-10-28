import random
import string

class Envio:
    contador = 0

    def __init__(self, distancia: float, peso: float):
        Envio.contador += 1
        self.distancia = distancia
        self.peso = peso
        self.precio = self.calcular_precio()
        self.codigo_rastreo = self.generar_codigo_rastreo()

    def calcular_precio(self) -> float:
        return self.distancia * self.peso * 0.5

    def generar_codigo_rastreo(self) -> str:
        codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return f"ENV-{codigo}"

    def mostrar_informacion(self) -> str:
        return f"Pedido:\n  Precio: {self.precio}\n  Código de rastreo: {self.codigo_rastreo}"
