# algoritmo para gestionar notas de estudiantes

# lista de notas ejemplo
notas = [3.5, 2.8, 4.0, 1.9, 3.0, 4.5]

# 1. recorrer y mostrar todas las notas
print("Notas de los estudiantes:")
for n in notas:
    print(n)

# 2. calcular promedio
suma = sum(notas)
promedio = suma / len(notas)
print("Promedio del grupo:", promedio)

# 3. modificar notas menores a 3.0 eje: subirlas 0.5 puntos
for i in range(len(notas)):
    if notas[i] < 3.0:
        notas[i] += 0.5

print("Notas ajustadas:", notas)

# 4. mostrar resultados consolidados
aprobados = [n for n in notas if n >= 3.0]
reprobados = [n for n in notas if n < 3.0]

print("Cantidad de aprobados:", len(aprobados))
print("Cantidad de reprobados:", len(reprobados))
