from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from data_processing.preprocess import load_data, preprocess_data
from models.train import train_model
from models.predict import predict_new_data
from visualizations.charts import create_charts

app = Flask(__name__)

# Variables globales
df_preprocessed = None
model = None
X_columns = None

# Ruta inicial de datos
DATA_PATH = 'data/AnalisisPlanos.csv'


@app.route('/')
def index():
    """Página principal."""
    global df_preprocessed
    if df_preprocessed is None:
        try:
            df = load_data(DATA_PATH)
            df_preprocessed = preprocess_data(df)
        except FileNotFoundError:
            pass
    return render_template('index.html')


@app.route('/visualize')
def visualize():
    """Visualización de los datos cargados."""
    if df_preprocessed is None:
        return redirect(url_for('index'))
    return render_template('visualize.html', data=df_preprocessed.to_html(classes="table table-striped"))


@app.route('/visualization/charts')
def visualize_charts():
    """Generar y visualizar gráficos."""
    global df_preprocessed

    if df_preprocessed is None:
        return redirect(url_for('index'))

    try:
        chart_paths, mae = create_charts(df_preprocessed)
        return render_template('charts.html', correlation_chart_path=chart_paths.get('correlation_matrix'),
                               comparison_chart_path=chart_paths.get('note_vs_difficulty'), mae=mae)
    except ValueError as e:
        return render_template('charts.html', error=str(e))


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """Subir y preprocesar un archivo CSV."""
    if request.method == 'POST':
        file = request.files['file']
        if file:
            try:
                global df_preprocessed
                df = load_data(file)
                df_preprocessed = preprocess_data(df)
                df_preprocessed.to_csv('data/preprocessed_data.csv', index=False)
                return render_template('upload.html', message="Datos cargados y preprocesados.", data=df_preprocessed.head().to_html(classes="table table-striped"))
            except Exception as e:
                return render_template('upload.html', error=f"Error al procesar el archivo: {e}")
    return render_template('upload.html')


@app.route('/train', methods=['GET', 'POST'])
def train():
    """Entrenar el modelo."""
    if request.method == 'POST':
        global model, X_columns

        if df_preprocessed is None:
            return render_template('train.html', error="No se han cargado datos para entrenar.")

        selected_model = request.form['model']

        if 'nota_estimada' not in df_preprocessed.columns or 'Tiempo preparacion + mecanizado' not in df_preprocessed.columns:
            return render_template('train.html', error="Faltan columnas necesarias en los datos preprocesados.")

        X = pd.get_dummies(df_preprocessed[['Material', 'Volumen', 'nota_estimada']], drop_first=True)
        y = df_preprocessed['Tiempo preparacion + mecanizado']

        try:
            model, results = train_model(X, y, selected_model)
            X_columns = X.columns
            return render_template('train.html', message=f"Modelo entrenado: {selected_model}. MSE: {results['mse']:.2f}, R²: {results['r2']:.2f}")
        except ValueError as e:
            return render_template('train.html', error=str(e))
    return render_template('train.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Realizar predicciones con el modelo."""
    if request.method == 'POST':
        if model is None:
            return render_template('predict.html', message="Primero entrena el modelo.")

        data = request.form.to_dict(flat=True)
        new_data = pd.DataFrame([data])
        new_data['Volumen'] = float(new_data['Volumen'])

        predictions = predict_new_data(model, new_data, X_columns)
        return render_template('predict.html', prediction=predictions[0])
    return render_template('predict.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
