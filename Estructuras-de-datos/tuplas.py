# La Tuplas no pueden modificarse una vez creadas.

# Para crear una tupla, encierra los elementos entre paréntesis.

punto = (3, 4)

# Para acceder a los elementos de una tupla, 
# utiliza el índice del elemento entre corchetes, 
# similar a las listas.

print(punto[0])  # Imprime 3

print(punto[1])  # Imprime 4

# Metodos predefinidos.


#  count(elemento): devuelve el número de veces que aparece un elemento en la tupla. 
#  index(elemento): devuelve el índice de la primera aparición de un elemento en la tupla. Opcionalmente, se puede especificar el inicio y fin de la búsqueda. 
#  len(tupla): aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla.


mi_tupla = (1, 2, 3, 2, 4, 2)


print (mi_tupla.index(2))   # Salida: 1

print (mi_tupla.index(2, 2))   #Salida: 3

print (mi_tupla.index(2, 2, 4))   #Salida: 3