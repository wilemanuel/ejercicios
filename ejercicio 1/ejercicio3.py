# Precio de una barra de pan y descuento
precio_barra = 2.5
descuento = 0.60

# Leer número de barras vendidas que no son del día
barras_no_dia = int(input("Número de barras vendidas que no son del día: "))

# Calcular precio final con descuento
coste_final = barras_no_dia * precio_barra * (1 - descuento)

# Mostrar resultados
print(f"Precio habitual: {precio_barra}€")
print(f"Descuento: {descuento * 100}%")
print(f"Coste final: {coste_final:.2f}€")