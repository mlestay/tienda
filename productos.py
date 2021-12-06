from typing import List

class productos:
    def __init__ (self, name_producto, precio_producto, categoria_producto, id_producto):
        self.name = name_producto
        self.precio = precio_producto
        self.categoria = categoria_producto
        self.id = id_producto

    def print_info(self):
        print(f"{self.name} es {self.categoria} y cuesta {self.precio}")
            
    def update_price(self, percent_change, is_increased):
        if is_increased == "sube":
            print(f"el nuevo precio es { (self.precio *percent_change) + self.precio }") 
            
        else:
            self.precio - (self.precio*percent_change) 
            print(f"el precio con descuento es {self.precio}")

    def inflation(self, percent_inflation):
        self.precio + (self.precio * percent_inflation)
        print (self.precio)

#  def set_clearence (self, categoria_producto, porcentaje_descuento):
