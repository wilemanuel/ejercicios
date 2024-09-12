# Solicitar peso y estatura al usuario
peso = float(input("Introduce tu peso en kilogramos: "))
estatura = float(input("Introduce tu estatura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Mostrar el IMC redondeado a dos decimales
print(f"Tu índice de masa corporal es {imc:.2f}")