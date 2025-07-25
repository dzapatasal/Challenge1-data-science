# -*- coding: utf-8 -*-
import sys
import io

# Establecer la codificación de salida estándar a UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

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

#1. ANALISIS DE FACTURACION
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

#_______________________________________________________________________________
#2. VENTAS POR CATEGORIA
# Configuracion para mostrar tabla completa
pd.set_option('display.expand_frame_repr', False)

# -- OBTENIENDO INGRESOS Y CANTIDADES --
# Obteniendo los ingresos y las cantidades (Ingresos por categoria)
ingresos_1 = tienda.groupby('Categoría del Producto')['Precio'].sum()
ingresos_2 = tienda2.groupby('Categoría del Producto')['Precio'].sum()
ingresos_3 = tienda3.groupby('Categoría del Producto')['Precio'].sum()
ingresos_4 = tienda4.groupby('Categoría del Producto')['Precio'].sum()

# Cantidad de productos vendidos por Categoría
conteo_1 = tienda['Categoría del Producto'].value_counts()
conteo_2 = tienda2['Categoría del Producto'].value_counts()
conteo_3 = tienda3['Categoría del Producto'].value_counts()
conteo_4 = tienda4['Categoría del Producto'].value_counts()

# -- CREANDO DATAFRAMES INDIVIDUALES COMBINADOS --
# Creando pares de columnas por tiendas
df_t1 = pd.concat([ingresos_1, conteo_1], axis=1)
df_t1.columns = ['Tienda 1', ' Cantidades T1']

df_t2 = pd.concat([ingresos_2, conteo_2], axis=1)
df_t2.columns = ['Tienda 2', ' Cantidades T2']

df_t3 = pd.concat([ingresos_3, conteo_3], axis=1)
df_t3.columns = ['Tienda 3', ' Cantidades T3']

df_t4 = pd.concat([ingresos_4, conteo_4], axis=1)
df_t4.columns = ['Tienda 4', ' Cantidades T4']

# -- UNIENDO 4 PARES Y ORDENANDO POR INGRESOS TOTALES --
# Unir todo por índice (Categoría del Producto)
df_unificado = pd.concat([df_t1, df_t2, df_t3, df_t4], axis=1)

# Calcular el total de ingresos (sin formatear aun) para ordenar
df_unificado['Total Ingresos'] = df_unificado[['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4']].sum(axis=1)

# Ordenar por total
df_ordenado = df_unificado.sort_values(by='Total Ingresos', ascending=False)

# -- Formatear ingressos con 'S/.' --
# Copiar para formatear sin afectar orden
df_final = df_ordenado.copy()

# Formatear solo columnas de ingresos
for col in ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4', 'Total Ingresos']:
  df_final[col] = df_final[col].map(lambda x: f'S/. {x:,}')

# -- RESULTADO --
print(df_final)
#_______________________________________________________________________________
#3. CALIFICACION PROMEDIO DE LAS TIENDAS

#TIENDA 1
calif_T1 = tienda['Calificación'].mean()
ventas_tienda = tienda['Precio'].sum()

#TIENDA 2
calif_T2 = tienda2['Calificación'].mean()
ventas_tienda_2 = tienda2['Precio'].sum()

#TIENDA 3
calif_T3 = tienda3['Calificación'].mean()
ventas_tienda_3 = tienda3['Precio'].sum()

#TIENDA 4
calif_T4 = tienda4['Calificación'].mean()
ventas_tienda_4 = tienda4['Precio'].sum()


# CONVERSION DE PARES A SERIES
s1 = pd.Series({'Promedio calificacion': calif_T1,'Total ventas': ventas_tienda},name='Tienda 1')
s2 = pd.Series({'Promedio calificacion': calif_T2,'Total ventas': ventas_tienda_2},name='Tienda 2')
s3 = pd.Series({'Promedio calificacion': calif_T3,'Total ventas': ventas_tienda_3},name='Tienda 3')
s4 = pd.Series({'Promedio calificacion': calif_T4,'Total ventas': ventas_tienda_4},name='Tienda 4')

resumen = pd.concat([s1, s2, s3, s4],axis=1) # Conserva los datos numericos originales, para calculos futuros.

# Si quieres mostrar las ventas formateadas como moneda, hazlo en una copia.
resumen_formateado = resumen.copy().astype(object)

# Opcional: Formatear las ventas con 'S/. ' y separador de miles.
# Aquí formateamos solo la fila de "Total ventas"
resumen_formateado.loc['Total ventas'] = resumen.loc['Total ventas'].apply(lambda x: f'S/. {x:,.2f}')

# La columna de calificaciones puede que no necesite un formato especial,
# pero podrías redondearla.
resumen_formateado.loc['Promedio calificacion'] = resumen.loc['Promedio calificacion'].apply(lambda x: f'{x:.2f}')

# Establecer un formato para todos los números de punto flotante
# '.2f' significa 2 decimales
pd.options.display.float_format = '{:,.2f}'.format


# -- VISUALIZACIÓN DEL DATAFRAME FORMATEADO --
# Esto te mostrará la tabla con un formato legible para el usuario.
print(resumen_formateado)

#_______________________________________________________________________________

# PRODUCTOS MAS Y MENOS VENDIDOS

# ENVIO PROMEDIO POR TIENDA