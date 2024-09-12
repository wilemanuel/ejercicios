# Solicitar un número entero impar y positivo
while True:
    altura = int(input("Introduce un número entero impar y positivo: "))
    if altura > 0 and altura % 2 != 0:
        break
    print("Por favor, introduce un número impar y mayor que 0.")

# Generar el triángulo
for i in range(1, altura + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=' ')
    print()  # Para pasar a la siguiente línea