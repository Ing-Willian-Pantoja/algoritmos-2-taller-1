import time

# crear una lista con muchos numeros
lista = list(range(1_000_000))

# medir tiempo de ejecución al elevar cada numero al cuadrado
inicio = time.time()
resultado = [x**2 for x in lista]
fin = time.time()

print("Tiempo usando lista:", fin - inicio, "segundos")
