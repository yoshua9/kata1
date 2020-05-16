"""
Escribir un programa que almacene la cadena de caracteres contrasñeas en una variable, preguntar al usuario por 
la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la
varible sin tener en cuenta mayúsculas y minúsculas.
"""

password = "contraseña"

password_del_usuario = input("Introduzca la contraseña: ")
password_del_usuario = password_del_usuario.lower()

if password == password_del_usuario:
    print("El password es correcto")
else:
    print("El password no coincide")
 