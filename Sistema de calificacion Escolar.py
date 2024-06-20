
# Introduce los datos del alumno
nombre_completo = input("Ingresa el nombre completo del alumno: ")
grado = input("Ingresa el grado del alumno: ")
grupo = input("Ingresa el grupo del alumno: ")

# Definir el número de materias
NUM_MATERIAS = 6

# Inicializar variables
sumatoria_calificaciones = 0

# Leer calificaciones de las materias
for i in range(NUM_MATERIAS):
    materia = input(f"Ingresa el nombre de la materia {i + 1}: ")
    calificacion = float(input(f"Ingresa la calificación de {materia}: "))
    sumatoria_calificaciones += calificacion

# Calculame el promedio
promedio = sumatoria_calificaciones / NUM_MATERIAS

# Imprimir resultados
print("\nDatos del alumno:")
print(f"Nombre completo: {nombre_completo}")
print(f"Grado: {grado}")
print(f"Grupo: {grupo}")
print(f"Promedio de calificaciones: {promedio:.2f}")
