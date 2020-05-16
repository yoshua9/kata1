"""
Creado u nprograma donde a partir de un numero, te devuelve su tabla de multiplicar
"""
#bool(digitales) true/false

#castear a int el dato que introduzca el usuario
tabla = input("Dime el número de la tabla de multiplicar")

try: 
    tabla = int(tabla)
except:
    print('Solo puede entrar numeros')

#range(x) -> Empieza por 0, y el número llega hasta X-1
#range(1,11,2) empieza en 1 y va de 2 en 2
if(isinstance(tabla,int)): 
    for i in range(11):
        print(str(tabla) + " x " + str(i) + " = " + str(tabla*i))
else:
    print("Solo puede introducir numeros")