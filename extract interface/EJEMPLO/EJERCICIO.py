class Envio:
    def calcular_precio(self, distancia: float, peso: float) -> float:
        return distancia * peso * 0.5

    def generar_rastreo(self) -> str:
        return "Código de rastreo generado."
