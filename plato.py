class Plato:
    def __init__(self, nombre: str, precio: float, descripcion: str ):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def detalles(self):
        desc = f"{self.nombre} - $ {self.precio:}"
        if self.descripcion:
            desc += f"   {self.descripcion}"
        return desc

    def __str__(self):
        return f"{self.nombre} ($ {self.precio:})"
#corto pero conciso el plato 
#este tiene 3 atributos principales nombre precio y descripcion
#ademas de 2 funciones detalles que muestra la informacion del plato y __str__ que devuelve una representacion simple del plato

#la funcion detalles devuelve una cadena con el nombre el precio y la descripcion del plato

#la funcion __str__ devuelve una cadena con el nombre y el precio del plato