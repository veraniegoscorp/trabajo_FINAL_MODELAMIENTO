
class Pedido:
    def __init__(self, comensal: 'comensal'):
        self.comensal = comensal
        self.platos: list = []
        self.estado = "CREADO" 

    def agregar_plato(self, plato: 'plato.Plato'):
        self.platos.append(plato)

    def quitar_plato_por_nombre(self, nombre: str):
        nombre = nombre.lower()
        for p in self.platos:
            if p.nombre.lower() == nombre:
                self.platos.remove(p)
                return True
        return False
    
    def total(self):
        return sum(p.precio for p in self.platos)

    def resumen(self):
        if not self.platos:
            return "(sin platos)"
        lines = [f"- {p.nombre}: $ {p.precio}" for p in self.platos]
        lines.append(f"TOTAL: $ {self.total()}")
        lines.append(f"ESTADO: {self.estado}")
        return "\n".join(lines)


    def marcar_listo(self):
        self.estado = "LISTO"

    def marcar_entregado(self):
        self.estado = "ENTREGADO"

    def marcar_pagado(self) :
        self.estado = "PAGADO"

#el pedido es la parte central del sistema ya que esta contiene la mayor parte de la logica del mismo
#este tiene funciones para agregar y quitar platos del pedido asi como para marcar el estado del mismo como por ejemplo listo entregado y pagado
#ademas de ciertas funciones para obtener el total y el resumen del pedido

#las funciones de agregar y quitar platos como su nombre lo indica siven para agregar y quitar platos del pedido

#las funcionen de total y resumen sirven para obtener el total del pedido y tener un resumen del mismo

#las funciones de marcar listo entregar y pagar sirven para cambiar el estado del pedido en cada una de sus etapas es nesesario para la logica del sistema
#ya que el mesero y el chef dependen del estado del pedido para realizar sus acciones