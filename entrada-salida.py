#Esta función muestra un mensaje en la pantalla y espera a que el usuario ingrese
# un valor.
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")


# print("Para mostrar información en la pantalla, utilizamos la función print().
#  Esta función toma uno o más argumentos y los muestra en la consola.

# Podemos utilizar la f-string (formateo de cadenas) para incrustar variables
# j
#  directamente dentro de una cadena de texto.Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

nombre = "Juan"
edad = 25


print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")