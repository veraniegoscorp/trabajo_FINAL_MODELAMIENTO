from plato import Plato
from comensal import Comensal
from mesero import Mesero
from chef import Chef
import time
# Catálogo simple (me dio flojera hacerlo mas grante xd)
CATALOGO = [
    Plato("milanesa", 5500, "con papas fritas"),
    Plato("ensalada", 3500, "mixta y fresca"),
    Plato("curry", 6000, "picante nivel medio"),
    Plato("sopa", 2800, "caldito casero"),
]


def mostrar_menu():
    print("menu del restaurante")
    time.sleep(0.5)
    print("1) Ver los platos")
    time.sleep(0.5)
    print("2) Ver detalles de un plato")
    time.sleep(0.5)
    print("3) Agregar plato al pedido")
    time.sleep(0.5)
    print("4) Quitar plato del pedido")
    time.sleep(0.5)
    print("5) Ver resumen del pedido")
    time.sleep(0.5)
    print("6) Enviar a cocina (preparar)")
    time.sleep(0.5)
    print("7) Entregar pedido")
    time.sleep(0.5)
    print("8) Pagar")
    time.sleep(0.5)
    print("0) Salir")


def elegir_plato_por_nombre(nombre: str):
    for p in CATALOGO:
        if p.nombre.lower() == nombre.lower():
            return p
    return None


def main():
    mesero = Mesero("cristian")
    chef = Chef("vicente")
    cliente = Comensal("juan carlos bodoque")

    while True:
        mostrar_menu()
        op = input("Elige una opción: ").strip()

        if op == "1":
            for p in CATALOGO:
                print(f"- {p}")
        elif op == "2":
            nombre = input("Nombre del plato: ").strip()
            plato = elegir_plato_por_nombre(nombre)
            if plato:
                print(plato.detalles())
            else:
                print("No existe ese plato.")
        elif op == "3":
            nombre = input("Nombre del plato a agregar: ").strip()
            plato = elegir_plato_por_nombre(nombre)
            if plato:
                cliente.pedir(plato, mesero)
                print(f"Agregado: {plato.nombre}")
            else:
                print("Plato no encontrado.")
        elif op == "4":
            nombre = input("Nombre del plato a quitar: ").strip()
            if cliente.cancelar_plato(nombre):
                print("Plato quitado del pedido.")
            else:
                print("No se pudo quitar (no está en el pedido o no hay pedido).")
        elif op == "5":
            print("RESUMEN:")
            print(cliente.ver_pedido())
        elif op == "6":
            if not cliente.pedido:
                print("Primero agrega platos.")
            else:
                chef.preparar(cliente.pedido)
                print(chef.revisar_pedido(cliente.pedido))
        elif op == "7":
            if not cliente.pedido:
                print("No hay pedido.")
            else:
                mesero.entregar_pedido(cliente.pedido)
        elif op == "8":
            try:
                monto = cliente.pagar()
                print(mesero.imprimir_ticket(cliente.pedido))
                print(f"\nPago realizado: ${monto:}")
            except Exception as e:
                print(f"No se pudo pagar: {e}")
        elif op == "0":
            print("muchas gracias por su visita")
            break
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    main()

