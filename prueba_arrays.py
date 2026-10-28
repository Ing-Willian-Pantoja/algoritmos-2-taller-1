import time
import numpy as np

# crear un array con muchos numeros
array = np.arange(1_000_000)

# medir tiempo de ejecución al elevar cada numero al cuadrado
inicio = time.time()
resultado = array**2
fin = time.time()

print("Tiempo usando array:", fin - inicio, "segundos")
