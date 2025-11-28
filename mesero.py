
class Mesero:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def crear_pedido(self, comensal: "Comensal"):
        print(f"{self.nombre} crea pedido para {comensal.nombre}")
        return Pedido(comensal)

    def entregar_pedido(self, pedido: "Pedido"):
        if pedido.estado != "LISTO":
            print("El pedido aún no está listo para entregar.")
            return
        else:
            pedido.marcar_entregado()
            print(f"{self.nombre} entrega el pedido a {pedido.comensal.nombre}")

    def imprimir_ticket(self, pedido:"Pedido"):
        tiket_mesero = f"Ticket - Mesero: {self.nombre} - Cliente: {pedido.comensal.nombre}"
        return tiket_mesero + pedido.resumen()

#el mesero es simple ya que este posee solamente 3 funciones principales las cuales son:

#crear un pedido para el comensal

#entregar el pedido al comensal cuando este listo en caso contrario se informa del estado del pedido

#eh por ultimo imprimir el ticket de atencion del pedido con el resumen del mismo