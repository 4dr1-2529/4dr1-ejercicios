from abc import ABC, abstractmethod

class IEnvio(ABC):
    @abstractmethod
    def calcular_precio(self, distancia: float, peso: float) -> float:
        pass

    @abstractmethod
    def generar_rastreo(self) -> str:
        pass
