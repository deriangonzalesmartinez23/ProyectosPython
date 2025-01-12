

#programa de recomendacion de vestimenta segun el cambio de clima.

def recomendacion_vestimenta(temperatura):
    if temperatura > 27:
        return "Hace calor. Viste ropa ligera y protégete del sol."
    elif 15 <= temperatura <= 27:
        return "El clima es templado. Usa camisetas o blusas con una chaqueta ligera."
    else:
        return "Hace frío. Ponte ropa abrigada y accesorios como bufanda y guantes."

# Solicitar la temperatura al usuario (puedes obtenerla de una fuente real en producción)
try:
    temperatura_actual = float(input("Ingresa la temperatura actual (°C): "))
    recomendacion = recomendacion_vestimenta(temperatura_actual)
    print(recomendacion)
except ValueError:
    print("Ingresa una temperatura válida en grados Celsius.")


