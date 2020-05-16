"""
Escribir un numero entero y mostrar un arbol en pantalla
"""

numero_arbol = input("Escribe el tamaño del arbol")

try: 
    numero_arbol = int(numero_arbol)
except:
    print('Solo puede entrar numeros')

#estrella = ""
if(isinstance(numero_arbol,int)):
    for i in range(numero_arbol):
        #estrella += "*"
        print('*' * (i+1))
else:
    print("Solo puede introducir numeros")