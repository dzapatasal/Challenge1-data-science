import pandas as pd
import os

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

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
