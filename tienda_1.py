from typing import List
from productos import productos

class tienda_1:
    def __init__ (self, name_tienda, listA):
        self.name = name_tienda
        self.listA = []
    
    def add_product (self, name_producto):
        self.listA.append(name_producto)
        print(f"Agregamos {name_producto}, los productos disponibles son {self.listA}")

    def sell_product (self, indice_lista):
        producto_vendido = self.listA.pop(indice_lista)
        print(f"Se vendió el {producto_vendido} y los productos disponibles son {self.listA}")
    
    def sell_product_byid (self, product_id):
        self.listA.pop(product_id)
        print(self.listA)
    
    def lista_disponible (self, name_tienda):
        print(self.listA)

#    def inflation(self,percent_increase): 

#    def set_clearence(self, category, percent_discount):



