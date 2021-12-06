from productos import productos
from tienda_1 import tienda_1

verduleria = tienda_1("verduleria", [])
tomate = productos("tomate", 200, "fruta", 1)
palta = productos ("palta", 500, "verdura", 2)
platano = productos ("platano", 100, "fruta", 3)
atun = productos ("atun_en_lata", 980, "no_perecible", 4)

verduleria.add_product("jamon")
tomate.print_info()
verduleria.lista_disponible(verduleria)











