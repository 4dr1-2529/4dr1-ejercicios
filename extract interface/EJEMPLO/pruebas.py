from envio import Envio

if __name__ == "__main__":
    # Lista de distancias y pesos para los ejemplos
    pedidos = [
        (10, 2),  # Distancia, Peso
        (15, 5),
        (8, 1),
        (20, 3),
        (7, 2),
        (25, 4),
        (30, 6),
        (12, 1),
        (9, 5),
        (14, 3),
        (12,4)
    ]

    # Crear y mostrar información de cada pedido
    for i, (distancia, peso) in enumerate(pedidos, start=1):
        envio = Envio(distancia, peso)
        print(f"Pedido {i}:")
        print(envio.mostrar_informacion())
        print()  # Línea en blanco para separar pedidos
