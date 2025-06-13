# 🎵 Proyecto: muzca-mel-to-style

Predicción del estilo musical (`style`) a partir del espectrograma Mel (`mel`), utilizando modelos de machine learning y deep learning, aplicando buenas prácticas de modularización, reproducibilidad y evaluación profesional.

---

## 📚 Tabla de Contenidos

- [📦 Requisitos e instalación](#-requisitos-e-instalación)
- [🚀 Ejecución del proyecto](#-ejecución-del-proyecto)
- [🔎 Exploración del Dataset](#-exploración-del-dataset)
- [🧠 Modelos y experimentos](#-modelos-y-experimentos)
- [📈 Métricas y evaluación](#-métricas-y-evaluación)
- [🗃️ Estructura del proyecto](#-estructura-del-proyecto)
- [🛠️ Créditos y mantenimiento](#-créditos-y-mantenimiento)

---

## 📦 Requisitos e instalación

```bash
# Crear entorno virtual
python -m venv .venv
.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt



🚀 Ejecución del proyecto
Se recomienda ejecutar el flujo desde el notebook 01_carga_y_exploracion.ipynb y continuar secuencialmente con los siguientes notebooks:

02_preprocesamiento.ipynb

03_modelos_base_regresion_mlp.ipynb

04_cnn_avanzada_attention.ipynb

05_optimizacion_bayesiana.ipynb

06_evaluacion_comparativa.ipynb

07_exportacion_modelo_final.ipynb

🔎 Exploración del Dataset
El archivo 01_carga_y_exploracion.ipynb se encarga de:

Verificar la estructura del archivo mel_fwod_dataset.npz, que contiene:

mel: espectrogramas Mel de cada muestra

meta: metadatos por muestra (incluye el campo style)

Contar los estilos musicales (style) presentes en el dataset

Generar la distribución de estilos mediante la función:

python
Copiar
Editar
from scripts.utils import guardar_distribucion_estilos
guardar_distribucion_estilos(style_counts, mostrar_en_notebook=True)
Esta función guarda:

📁 results/style_distribution.csv

🖼️ images/distribucion_estilos.png

Y muestra el gráfico directamente dentro del notebook (opcional con mostrar_en_notebook=True)

🧠 Modelos y experimentos
Cada modelo se define en un notebook separado. Para cada modelo se sigue una estructura clara y repetible:

Entrenamiento del modelo

Evaluación con métricas

Exportación del modelo .pt

Registro de resultados

Comparación con modelos anteriores

Análisis de errores por clase

Visualización cualitativa

Reflexión o reentrenamiento documentado

📈 Métricas y evaluación
El proyecto incluye evaluación con métricas específicas para clasificación multiclase:

Accuracy

Precision

Recall

F1-score

Matriz de confusión

Visualización de errores por clase (style)

También se analiza el impacto de modelos base vs avanzados.

🗃️ Estructura del proyecto
text
Copiar
Editar
data/          ← Dataset original (.npz)
scripts/       ← Funciones reutilizables y utilitarias
checkpoints/   ← Modelos exportados (.pt)
results/       ← Resultados de métricas (.csv, .json)
images/        ← Gráficos generados automáticamente
logs/          ← Logs estructurados (si aplica)
backups/       ← Respaldos automáticos con timestamp
notebooks/     ← (opcional si se separan de la raíz)
🛠️ Créditos y mantenimiento
Proyecto desarrollado por Alfredo Aponte como parte de su tesis.
Repositorio oficial en GitHub:
🔗 https://github.com/ajapontes/muzca-mel-to-style