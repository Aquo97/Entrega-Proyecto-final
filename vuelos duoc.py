import numpy as np
import asientos as en
op1 = 0

while op1 != 1:
 try:
    print(" ***Vuelos-Duoc***")
    print("    ---MENU---")
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")
    op1 = int(input("Seleccione una opcion: "))
 except:
   print("TIENE QUE INGRESAR UNA DE LAS OPCIONES")


 if op1 == 1:
     print(en)
