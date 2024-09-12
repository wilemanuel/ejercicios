# Precio de una barra de pan
precio_barra = 2.5

# Descuento para pan que no es del día (60%)
descuento = 0.60

# Solicitar al usuario la cantidad de barras que no son del día
barras_no_dia = int(input("Introduce la cantidad de barras que no son del día: "))

# Calcular el precio con descuento
precio_final = barras_no_dia * precio_barra * (1 - descuento)

# Mostrar el precio final
print(f"El precio total por {barras_no_dia} barras que no son del día es: {precio_final:.2f}€")