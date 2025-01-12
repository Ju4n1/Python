#Para leer el contenido de un archivo, primero debemos abrirlo utilizando 
# la función open() en modo de lectura ("r"). Luego, podemos leer el 
# contenido del archivo utilizando métodos como read() o readlines().

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

# Escritura en archivos.
archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

# Obtener y mostrar contenido archivo.
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)