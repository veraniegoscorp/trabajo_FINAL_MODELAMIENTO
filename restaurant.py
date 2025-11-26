from clases_restaurante import *

def main():

    # --- Crear menú de platos ---
    menu = [
        Plato("Pizza", "Masa fina con salsa y queso", 9000),
        Plato("Hamburguesa", "Con papas y bebida", 8500),
        Plato("Ensalada César", "Pollo, lechuga y salsa", 7500),
    ]

    app = Aplicacion()
    cliente = Cliente("Juan")
    pedido = None
    mesero = Mesero("Carlos")

    while True:
        print("\n====== SISTEMA DEL RESTAURANTE ======")
        print("1. Ver menú de platos")
        print("2. Crear pedido")
        print("3. Agregar plato al pedido")
        print("4. Asignar mesero")
        print("5. Enviar a cocina")
        print("6. Mostrar total")
        print("7. Registrar pago")
        print("8. Entregar pedido")
        print("9. Ver estado del pedido")
        print("0. Salir")

        opcion = input(" Elige una opción: ")

        if opcion == "1":
            cliente.ver_menu(menu)

        elif opcion == "2":
            pedido = cliente.crear_pedido()
            print(" Pedido creado exitosamente.")

        elif opcion == "3":
            if pedido is None:
                print("Primero debes crear un pedido.")
                continue

            print("\n=== Elige un plato ===")
            for i, plato in enumerate(menu):
                print(f"{i+1}. {plato.mostrar_caracteristicas()}")

            eleccion = int(input("Número del plato: ")) - 1
            if 0 <= eleccion < len(menu):
                pedido.agregar_plato(menu[eleccion])
                print("Plato agregado.")
            else:
                print(" Opción inválida.")

        elif opcion == "4":
            if pedido is None:
                print("Primero debes crear un pedido.")
                continue

            pedido.asignar_mesero(mesero)
            print(f"Mesero {mesero.nombre} asignado.")

        elif opcion == "5":
            if pedido is None:
                print("Primero debes crear un pedido.")
                continue

            mesero.recibir_pedido(pedido)
            app.ingresar_en_cocina(pedido)

        elif opcion == "6":
            if pedido is None:
                print("Primero debes crear un pedido.")
                continue

            app.mostrar_total(pedido)

        elif opcion == "7":
            if pedido is None:
                print("Primero debes crear un pedido.")
                continue

            app.recibir_pago(pedido)

        elif opcion == "8":
            if pedido is None:
                print("Primero debes crear un pedido.")
                continue

            mesero.entregar_pedido(pedido)

        elif opcion == "9":
            if pedido is None:
                print("⚠ Primero debes crear un pedido.")
                continue

            print(f"Estado actual: {pedido.mostrar_estado()}")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    main()
