# scripts/utils.py (versión mejorada)

import os
import pandas as pd
import matplotlib.pyplot as plt

def guardar_distribucion_estilos(
    style_counts,
    nombre_csv='results/style_distribution.csv',
    nombre_img='images/distribucion_estilos.png',
    mostrar_en_notebook=True
):
    """
    Guarda la distribución de estilos en CSV e imagen, y opcionalmente la muestra en el notebook.

    Parámetros:
    - style_counts (collections.Counter): contador de estilos
    - nombre_csv (str): ruta del archivo CSV a guardar
    - nombre_img (str): ruta del archivo de imagen PNG
    - mostrar_en_notebook (bool): si True, muestra el gráfico en el notebook
    """

    # Convertir a DataFrame
    df = pd.DataFrame(style_counts.items(), columns=['style', 'count'])
    df = df.sort_values(by='count', ascending=False)

    # Guardar CSV
    os.makedirs(os.path.dirname(nombre_csv), exist_ok=True)
    df.to_csv(nombre_csv, index=False)
    print(f"📁 Archivo CSV guardado en: {nombre_csv}")

    # Crear gráfico
    plt.figure(figsize=(12, 6))
    plt.bar(df['style'], df['count'], color='skyblue')
    plt.xticks(rotation=90, fontsize=8)
    plt.title('Distribución de Estilos Musicales')
    plt.xlabel('Estilo')
    plt.ylabel('Cantidad de muestras')
    plt.tight_layout()

    # Guardar imagen
    os.makedirs(os.path.dirname(nombre_img), exist_ok=True)
    plt.savefig(nombre_img)
    print(f"🖼️ Imagen guardada en: {nombre_img}")

    # Mostrar en notebook si se desea
    if mostrar_en_notebook:
        plt.show()
    else:
        plt.close()
