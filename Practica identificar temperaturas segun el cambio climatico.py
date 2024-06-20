

def clasificar_temperatura(temperatura):
    if temperatura > 25:
        return "Caluroso: ¡Protégete del sol y mantente hidratado!"
    elif 15 <= temperatura <= 25:
        return "Templado: Disfruta del clima agradable."
    else:
        return "Frío: Abrígate y prepárate para posibles precipitaciones."

# Solicitar la temperatura al usuario (puedes obtenerla de una fuente real en producción)
try:
    temperatura_actual = float(input("Ingresa la temperatura actual (°C): "))
    clasificacion = clasificar_temperatura(temperatura_actual)
    print(f"Clasificación del clima: {clasificacion}")
except ValueError:
    print("Ingresa una temperatura válida en grados Celsius.")
