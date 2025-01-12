# Para definir una función en Python, utilizamos la palabra clave 
# def seguida del nombre de la función y paréntesis.
def saludo():
    print("¡Hola, mundo!")


saludo()  # Imprime "¡Hola, mundo!"


# Funcion con parametros yretornos.
def suma(a, b):
    return a + b


resultado = suma(3, 4)
print(resultado)  # Imprime 7

# Funciones anónimas o funciones lambda, que son funciones sin nombre 
# definidas en una sola línea. Se utilizan comúnmente para funciones 
# pequeñas y concisas.
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25