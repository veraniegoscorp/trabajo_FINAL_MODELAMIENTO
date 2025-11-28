class Comensal:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.pedido = None

    def pedir(self, plato: "plato", mesero: "mesero"):
        if not self.pedido:
            self.pedido = mesero.crear_pedido(self)
        self.pedido.agregar_plato(plato)

    def ver_pedido(self):
        if not self.pedido:
            return "no hay un pedido echo por esta mesa o comensal"
        return self.pedido.resumen()

    def cancelar_plato(self, nombre_plato: str):
        if not self.pedido:
            return False
        return self.pedido.quitar_plato_por_nombre(nombre_plato)

    def pagar(self):
        monto = self.pedido.total()
        self.pedido.marcar_pagado()
        return monto
#comensal es quien hace el pedido y lo termina al pagar
#este tiene 4 funciones principales 
#las cuales son pedir que es para agregar platos al pedido

#ver el pedido que muestra el resumen del mismo

#cancelar plato que quita un plato del pedido pero solo si este mismo existe (para que no se pueda quitar un plato que no existe)

#y pagar que marca el pedido como pagado y retorna el monto aparte de terminar el flujo del sistema.