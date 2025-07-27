# -*- coding: utf-8 -*-
import sys
import io
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.patches import Patch

# Establecer la codificación de salida estándar a UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# IMPORTACION DE DATOS DE ALURA STORE LATAM
import pandas as pd
import os

# URLs proporcionadas por ALURA
# url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
# url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
# url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
# url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

# Carga del archivo CSV alojado en una URL de todas las tiendas
tienda = pd.read_csv("tienda_1.csv")
tienda2 = pd.read_csv("tienda_2.csv")
tienda3 = pd.read_csv("tienda_3.csv")
tienda4 = pd.read_csv("tienda_4.csv")

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
# ANÁLISIS COMPARATIVO DE PRODUCTOS MÁS Y MENOS VENDIDOS POR TIENDA

# Para cada tienda, se cuenta cuántas veces se vendió cada producto y se ordenan de mayor a menor.
# Se convierte el resultado a un DataFrame con columnas renombradas para claridad.

conteo_items_T1 = tienda['Producto'].value_counts().reset_index()
conteo_items_T1.columns = ['Producto T1', 'Cantidad T1']  # Producto más vendido de la Tienda 1

conteo_items_T2 = tienda2['Producto'].value_counts().reset_index()
conteo_items_T2.columns = ['Producto T2', 'Cantidad T2']  # Producto más vendido de la Tienda 2

conteo_items_T3 = tienda3['Producto'].value_counts().reset_index()
conteo_items_T3.columns = ['Producto T3', 'Cantidad T3']  # Producto más vendido de la Tienda 3

conteo_items_T4 = tienda4['Producto'].value_counts().reset_index()
conteo_items_T4.columns = ['Producto T4', 'Cantidad T4']  # Producto más vendido de la Tienda 4

# Se combinan los DataFrames horizontalmente (por columnas), comparando por posición de fila (no por nombre de producto).
# Esto permite comparar directamente el ranking de productos más vendidos entre tiendas.
df_unificado_items = pd.concat(
    [conteo_items_T1, conteo_items_T2, conteo_items_T3, conteo_items_T4],
    axis=1
)

# Se muestra la tabla consolidada para análisis visual o exportación.
print(df_unificado_items)

#----------------------------------------------------------------------------
# ENVIO PROMEDIO POR TIENDA

def mostrar_promedios_flete(tiendas):
    print("Promedio del costo de envío por tienda:")
    for i, df in enumerate(tiendas, start=1):
        promedio = df['Costo de envío'].mean()
        print(f"  Tienda T{i}: S/ {promedio:.2f}")

# Llamada
mostrar_promedios_flete([tienda, tienda2, tienda3, tienda4])

#-----------------------------------------------------------------------------
# GRAFICA 1
# Crear un DataFrame manual con esos subtotales
df_grf_1 = pd.DataFrame({
   'Tienda': ['Nro. 1', 'Nro. 2', 'Nro. 3', 'Nro. 4'],
   'Ventas': [subTotal_ventas_tienda, 
              subTotal_ventas_tienda2, 
              subTotal_ventas_tienda3, 
              subTotal_ventas_tienda4
              ]   
})

# Colores personalizados por barra
colores =['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Azul, naranja, verde, rojo

# Creacion de grafico
fig, ax = plt.subplots(figsize =(8, 6))
barras = ax.bar(df_grf_1['Tienda'], df_grf_1['Ventas'], color=colores)

# Mostrar eje Y en millones (ajuste a 1e9 si son miles de millones)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x/1e6:.1f}M'))

# Titulos & Etiquetas
plt.title('Ingreso total de ventas por Tienda')
plt.xlabel('Tienda')
plt.ylabel(' Ventas (S/.)\nMiles de millones')

# Mostrar el monto exacto encima de cada barra
for i,v in enumerate(df_grf_1['Ventas']):
   ax.text(i, v + (v*0.01),f"S/. {v:,.2f}",ha='center', va='bottom', fontsize=9)


plt.tight_layout

# [GRAFICA 2] 
# Todas las categorías únicas
todas_categorias = sorted(set(conteo_1.index) | set(conteo_2.index) | set(conteo_3.index) | set(conteo_4.index))

# Generar abreviaturas para cada categoría (iniciales o primera sílaba)
abreviaturas = {cat: ''.join([p[0] for p in cat.split()]).upper() for cat in todas_categorias}

# Asignar colores consistentes por categoría
colores_base = plt.cm.tab20.colors
colores_categoria = {cat: colores_base[i % len(colores_base)] for i, cat in enumerate(todas_categorias)}

# Listas de conteos y nombres de tiendas
conteos = [conteo_1, conteo_2, conteo_3, conteo_4]
nombres_tiendas = ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4']

# Crear subplots
fig, axes = plt.subplots(1, 4, figsize=(22, 6))

for i, ax in enumerate(axes):
    conteo = conteos[i].reindex(todas_categorias, fill_value=0)
    proporciones = conteo / conteo.sum()
    proporciones = proporciones.sort_values(ascending=False)

    sizes = proporciones.values
    categorias_ordenadas = proporciones.index
    labels = [abreviaturas[cat] for cat in categorias_ordenadas]
    colors = [colores_categoria[cat] for cat in categorias_ordenadas]

    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.set_title(nombres_tiendas[i])

# Crear leyenda común (fuera del gráfico)
leyenda_patches = [
    Patch(facecolor=colores_categoria[cat], label=f"{abreviaturas[cat]} = {cat}")
    for cat in todas_categorias
]

# Posicionar leyenda debajo de los gráficos
fig.legend(handles=leyenda_patches, loc='lower center', ncol=4, fontsize=10)
plt.subplots_adjust(bottom=0.2)

# Título general
plt.suptitle('Distribución porcentual de productos vendidos por categoría (con abreviaturas)', fontsize=16)
plt.tight_layout()
plt.show()


