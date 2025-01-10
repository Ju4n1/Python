

# Crea lista.

frutas = ["manzana", "banana", "naranja"]

# Accede elemenos.
print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "naranja"

# Acceso en orden inverso.
print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"

# Metodos predefinidos.


# Inserta al final de la lista.
frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]

# Inserta en un posición predefinida.
frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

# Elimina la primer aparicion del elemento en la lista.
frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

# Elimina y retorna el elemento n un posición específica.
fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

# Ordena la lista.
frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]

# Invierte el orden de la lista.
frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

# Listas de comprensión.

#nueva_lista = [expresion for elemento in secuencia if condicion]

numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0] #"**2 eleva al cuadrado"
print(cuadrados)  # Imprime [4, 16]