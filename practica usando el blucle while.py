def suma_de_numeros():
    suma_total = 0
    numero = 1

    while numero <= 10:
        suma_total += numero
        numero += 1

    print(f"La suma de los números del 1 al 10 es: {suma_total}")

# Llamamos a la función para obtener el resultado
suma_de_numeros()
