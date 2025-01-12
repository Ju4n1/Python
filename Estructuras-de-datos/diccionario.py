# Para crear un diccionario, utiliza llaves y separa las claves
#  y valores con dos puntos.

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

# Para acceder a los valores de un diccionario, utiliza la clave
#  correspondiente entre corchetes.

print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
print(persona["ciudad"])  # Imprime "Madrid"

# Metodos predefinidos.

    #keys(): devuelve una vista de todas las claves del diccionario.
    #values(): devuelve una vista de todos los valores del diccionario.
    #items(): devuelve una vista de todos los pares clave-valor del diccionario.
    #update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.

# Ejemplo.

print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])


persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}

 