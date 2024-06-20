def suma_de_dos_numeros():
    try:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
        resultado = numero1 + numero2
        print(f"La suma de {numero1} y {numero2} es: {resultado}")
    except ValueError:
        print("Ingresa números válidos.")

# Llamamos a la función imprimir los resultado
suma_de_dos_numeros()
