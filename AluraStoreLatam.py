# IMPORTACION DE DATOS DE ALURA STORE LATAM
import pandas as pd
import os

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

# Carga del archivo CSV alojado en una URL de todas las tiendas
tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

# Guardar los archivos en disco
tienda.to_csv("tienda_1.csv", index=False)
tienda2.to_csv("tienda_2.csv", index=False)
tienda3.to_csv("tienda_3.csv", index=False)
tienda4.to_csv("tienda_4.csv", index=False)

# Abrir los archivos CSV en el explorador de archivoS
os.startfile("tienda_1.csv")
os.startfile("tienda_2.csv")
os.startfile("tienda_3.csv")
os.startfile("tienda_4.csv")

# ANALISIS DE FACTURACION
# Suma de los valores de la columna 'Precio' de todas las tiendas
subTotal_ventas_tienda = tienda['Precio'].sum()
subTotal_ventas_tienda2 = tienda2['Precio'].sum()
subTotal_ventas_tienda3 = tienda3['Precio'].sum()
subTotal_ventas_tienda4 = tienda4['Precio'].sum()

# Suma de todas las tiendas
Total_ventas = subTotal_ventas_tienda + subTotal_ventas_tienda2 + subTotal_ventas_tienda3 + subTotal_ventas_tienda4

# Mostrar contenido
# (variable:,) → formateando el numero para que tenga comas como separadores de miles

print("Total de ventas")
print(f'Tienda 1: S/. {subTotal_ventas_tienda:,}')
print(f'Tienda 2: S/. {subTotal_ventas_tienda2:,}')
print(f'Tienda 3: S/. {subTotal_ventas_tienda3:,}')
print(f'Tienda 4: S/. {subTotal_ventas_tienda4:,}')

print(f'Total de ventas (4 Tiendas) : S/. {Total_ventas:,}')

# VENTAS POR CATEGORIA

# CALIFICACION PROMEDIO DE LAS TIENDAS

# PRODUCTOS MAS Y MENOS VENDIDOS

# ENVIO PROMEDIO POR TIENDA