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

def guardar_resumen_meta(meta_array, path_csv='results/meta_summary.csv', mostrar_en_notebook=True):
    """
    Genera y guarda un resumen estadístico del campo `meta` como archivo CSV, y opcionalmente lo muestra en el notebook.

    Parámetros:
    - meta_array (np.ndarray): arreglo de diccionarios `meta`
    - path_csv (str): ruta donde se guarda el archivo CSV
    - mostrar_en_notebook (bool): si True, muestra el resumen como tabla en el notebook
    """
    import pandas as pd
    import os

    df = pd.DataFrame(meta_array.tolist())

    resumen = pd.DataFrame({
        'Campo': df.columns,
        'Valores únicos': [df[col].nunique() for col in df.columns],
        'Tipo de dato': [df[col].dtype for col in df.columns],
        'Muestras no nulas': [df[col].notnull().sum() for col in df.columns]
    })

    os.makedirs(os.path.dirname(path_csv), exist_ok=True)
    resumen.to_csv(path_csv, index=False)
    print(f"📄 Resumen guardado en: {path_csv}")

    if mostrar_en_notebook:
        from IPython.display import display, Markdown
        display(resumen)
        # Mostrar como tabla Markdown
        markdown_table = resumen.to_markdown(index=False)
        print("\n📋 Resumen en formato Markdown:\n")
        print(markdown_table)

def guardar_y_mostrar_figura(fig, path_img):
    """
    Guarda y muestra una figura matplotlib.
    
    Parámetros:
    - fig: objeto figura matplotlib
    - path_img (str): ruta completa donde se guardará la imagen
    """
    import os

    os.makedirs(os.path.dirname(path_img), exist_ok=True)
    fig.savefig(path_img)
    print(f"🖼️ Imagen guardada en: {path_img}")
    plt.show()

def respaldar_y_limpiar_directorios(directorios, backup_dir='backups'):
    """
    Comprime el contenido de los directorios indicados en un .zip de respaldo y limpia las carpetas.

    Parámetros:
    - directorios (list): lista de carpetas a respaldar
    - backup_dir (str): carpeta donde se guardan los .zip de respaldo
    """
    import zipfile
    import shutil
    import os
    from datetime import datetime

    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_path = os.path.join(backup_dir, f'backup_{timestamp}.zip')

    # Crear el archivo ZIP solo con los directorios indicados
    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zipf:
        for directory in directorios:
            directory = directory.strip()
            if os.path.exists(directory):
                for root, _, files in os.walk(directory):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, start='.')
                        zipf.write(file_path, arcname)

    print(f"✅ Backup creado: {zip_path}")

    # Limpiar las carpetas indicadas
    for d in directorios:
        d = d.strip()
        if os.path.exists(d):
            for file in os.listdir(d):
                file_path = os.path.join(d, file)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"⚠️ No se pudo eliminar {file_path}: {e}")

def generar_comparacion_modelos(
    results_dir='results',
    output_image_path=None,
    top_n_models=None,
    show_plot=True
):
    """
    Genera un gráfico comparativo de las métricas clave de los modelos evaluados.

    Args:
        results_dir (str): Directorio donde se encuentran los archivos de métricas.
        output_image_path (str): Ruta para guardar el gráfico generado.
        top_n_models (int): Limitar a los N primeros modelos encontrados (opcional).
        show_plot (bool): Si True, muestra el gráfico en el notebook.
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import json
    import glob
    import os
    from datetime import datetime

    files = glob.glob(os.path.join(results_dir, "metrics_*.json"))
    data = []
    for file in files:
        with open(file, 'r') as f:
            metrics = json.load(f)
            modelo = os.path.basename(file).replace("metrics_", "").replace(".json", "")
            data.append({
                "modelo": modelo,
                "test_accuracy": metrics.get("test_accuracy"),
                "test_balanced_accuracy": metrics.get("test_balanced_accuracy"),
                "f1_macro": metrics.get("test_f1_macro"),
                "f1_weighted": metrics.get("test_f1_weighted")
            })

    df = pd.DataFrame(data)
    if df.empty:
        print("⚠ No se encontraron métricas para graficar.")
        return

    if top_n_models:
        df = df.head(top_n_models)

    # Graficar
    df_melt = df.melt(id_vars="modelo", var_name="métrica", value_name="valor")
    plt.figure(figsize=(10,6))
    sns.barplot(data=df_melt, x="modelo", y="valor", hue="métrica")
    plt.title("Comparación de modelos")
    plt.ylabel("Valor")
    plt.xlabel("Modelo")
    plt.legend(title="Métrica")
    plt.tight_layout()

    # Guardar
    if not output_image_path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_image_path = f"images/model_comparison_{timestamp}.png"
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    plt.savefig(output_image_path)
    if show_plot:
        plt.show()
    else:
        plt.close()

    print(f"📂 Imagen comparativa guardada en: {output_image_path}")
