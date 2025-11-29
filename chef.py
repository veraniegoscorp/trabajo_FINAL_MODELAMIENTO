
class Chef:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def preparar(self, pedido: 'Pedido'):        
        
        print(f"{self.nombre} está preparando el pedido...")
        
        pedido.marcar_listo()

        print(f"{self.nombre} terminó: pedido LISTO")

    def revisar_pedido(self, pedido: 'Pedido'):
        
        return f"Chef {self.nombre} ve estado: {pedido.estado}"

# explicacion el chef puede preparar pedidos entonces el puede marcar el estado del pedido como listo para que el mesero lo entrege al comensal
# y tambien puede ver el estado del pedido asi no tenemos 2 chefs haciendo lo mismo