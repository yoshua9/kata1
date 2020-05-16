   
"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%.
Escribe un programa que comience leyendo el número de barras vendidas que no son del día. Después tu programa
debe mostrar el precio habitual de una barra de pan, el descuente que se le hace por no ser fresca y el coste
final total.
"""

precio = 3.49
descuento = 0.4
precio_con_descuento = precio * descuento

numero_de_barras = input("Introduce el número de barras vendidas:")
numero_de_barras = int(numero_de_barras)

print("Precio habitual: "+ str(precio))
print("Precio con descuento: "+ str(precio_con_descuento))
print("Precio total: "+ str(precio_con_descuento * numero_de_barras))