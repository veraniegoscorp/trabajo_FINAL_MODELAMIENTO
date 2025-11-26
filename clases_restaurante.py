
class Plato():
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def mostrar_caracteristicas(self):
        return f"{self.nombre}: {self.descripcion} - ${self.precio}"


class Pedido():
    def __init__(self, cliente):
        self.cliente = cliente
        self.platos = []
        self.mesero = None
        self.pagado = False
        self.estado = "Pendiente"

    def agregar_plato(self, plato):
        self.platos.append(plato)

    def asignar_mesero(self, mesero):
        self.mesero = mesero
        self.estado = "Con mesero asignado"

    def calcular_total(self):
        return sum(plato.precio for plato in self.platos)

    def registrar_pago(self):
        self.pagado = True
        self.estado = "Pagado"

    def mostrar_estado(self):
        return self.estado


class Cliente():
    def __init__(self, nombre):
        self.nombre = nombre

    def ver_menu(self, menu):
        print("=== MENU DISPONIBLE ===")
        for plato in menu:
            print(plato.mostrar_caracteristicas())

    def crear_pedido(self):
        return Pedido(self)


class Mesero():
    def __init__(self, nombre):
        self.nombre = nombre

    def recibir_pedido(self, pedido):
        pedido.estado = "Recibido por cocina"
        print(f"El mesero {self.nombre} recibió el pedido.")

    def entregar_pedido(self, pedido):
        pedido.estado = "Entregado al cliente"
        print(f"El mesero {self.nombre} entregó el pedido.")


class Aplicacion():
    def registrar_pedido(self, pedido):
        print("Pedido registrado en el sistema.")

    def mostrar_total(self, pedido):
        print(f"Total a pagar: ${pedido.calcular_total()}")

    def ingresar_en_cocina(self, pedido):
        pedido.estado = "En cocina"
        print("Pedido enviado a cocina.")

    def recibir_pago(self, pedido):
        pedido.registrar_pago()
        print("Pago registrado con éxito.")
