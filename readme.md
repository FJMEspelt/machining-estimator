Estimador de Tiempo de Mecanizado
Esta aplicación Flask permite analizar, preprocesar, visualizar datos y realizar predicciones relacionadas con la eficiencia en mecanizado. Proporciona una interfaz para cargar datos, entrenar modelos de Machine Learning y generar gráficos interactivos.

## **Estructura del Proyecto**

```plaintext
app/
├── app.py
├── models/
│   ├── train.py               # Entrenamiento de modelos de ML
│   ├── evaluate.py            # Evaluación de modelos (opcional)
│   └── predict.py             # Predicciones usando modelos entrenados
├── data_processing/
│   └── preprocess.py          # Preprocesamiento de datos
├── visualizations/
│   └── charts.py              # Generación de gráficos
├── templates/
│   ├── charts.html            # Página para visualizar gráficos
│   ├── index.html             # Página principal
│   ├── predict.html           # Página de predicción
│   ├── train.html             # Página de entrenamiento
│   ├── upload.html            # Página de subida de datos
│   ├── visualize.html         # Página de visualización de datos
├── static/
│   ├── css/
│   │   └── style.css          # Estilos CSS para la aplicación
│   └── charts/                # Carpeta para guardar gráficos generados
└── data/
    └── AnalisisPlanos.csv     # Archivo de datos inicial (opcional)
```

Características
    Carga de Datos: Subida de archivos CSV para análisis.
    Preprocesamiento: Limpieza y transformación automática de datos cargados.
    Entrenamiento de Modelos: Entrena modelos de Machine Learning (Linear Regression, Random Forest, SVM).
    Visualización de Gráficos:
        Matriz de correlación.
        Comparación de Nota Estimada vs Dificultad.
    Predicción: Realiza predicciones usando modelos entrenados.

Instalación

Clona este repositorio:
    git clone https://github.com/usuario/estimador-mecanizado.git
    cd estimador-mecanizado/app

Instala las dependencias necesarias:
    pip install -r requirements.txt

Coloca tu archivo de datos inicial en data/AnalisisPlanos.csv.

Uso
Ejecuta la aplicación Flask:
    python app.py

Abre el navegador y accede a:
    http://127.0.0.1:5000

Flujo Principal:

    Visualizar Datos: Navega a /visualize para ver los datos cargados.
    Subir Datos: Ve a /upload para cargar un nuevo archivo CSV.
    Entrenar Modelos: Selecciona y entrena un modelo en /train.
    Visualizar Gráficos: Genera gráficos desde /visualization/charts.
    Predicciones: Realiza predicciones desde /predict.

Requisitos
    Python: >= 3.8

Bibliotecas:
    Flask
    pandas
    numpy
    matplotlib
    seaborn
    scikit-learn

Funciones Modulares:

1. Preprocesamiento (data_processing/preprocess.py)
    Carga y transforma datos para análisis y modelos de ML.

2. Entrenamiento de Modelos (models/train.py)
Entrena modelos como Linear Regression, Random Forest y SVM.

3. Predicciones (models/predict.py)
Realiza predicciones basadas en datos ingresados.

4. Gráficos (visualizations/charts.py)
Genera gráficos como la matriz de correlación y comparaciones.

Capturas de Pantalla

    Página Principal

    Gráficos Generados

Mejoras Futuras
    Implementar más modelos de Machine Learning.
    Agregar validaciones avanzadas para los datos cargados.
    Mejorar la interfaz gráfica con frameworks como Bootstrap.

Licencia
    Este proyecto está bajo la Licencia MIT. Puedes usar, modificar y distribuir libremente.

Contacto
    Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

Email: javiespelt@gmail.com
