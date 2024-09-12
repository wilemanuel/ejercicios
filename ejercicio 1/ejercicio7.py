# Solicitar un número entero positivo
numero = int(input("Introduce un número entero positivo: "))

# Generar la cuenta atrás y mostrarla
cuenta_atras = ', '.join(str(i) for i in range(numero, -1, -1))

# Mostrar la cuenta atrás
print(cuenta_atras)