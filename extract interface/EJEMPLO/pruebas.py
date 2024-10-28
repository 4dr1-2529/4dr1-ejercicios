from envio import Envio

if __name__ == "__main__":

    pedidos = [
        (10, 2),
        (15, 5),
        (8, 1),
        (20, 3),
        (7, 2),
        (25, 4),
        (30, 6),
        (12, 1),
        (9, 5),
        (14, 3),
        (12,1)
    ]


    for i, (distancia, peso) in enumerate(pedidos, start=1):
        envio = Envio(distancia, peso)
        print(f"Pedido {i}:")
        print(envio.mostrar_informacion())
        print()
