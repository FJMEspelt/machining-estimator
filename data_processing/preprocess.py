import pandas as pd

def load_data(file_path: str, delimiter: str = ';', encoding: str = 'latin1') -> pd.DataFrame:
    """Carga un archivo CSV y lo devuelve como DataFrame."""
    return pd.read_csv(file_path, delimiter=delimiter, encoding=encoding)

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocesa el DataFrame: limpia los datos y calcula columnas adicionales si es necesario."""
    # Crear la columna 'nota_estimada' si no existe
    if 'nota_estimada' not in df.columns:
        df['nota_estimada'] = df.apply(
            lambda row: nota_estimada(row['Material'], row['Tolerancia'], row['Volumen'], row['Operaciones']), axis=1
        )
    return df

def nota_estimada(material, tolerancia, volumen, operaciones):
    """Calcula la nota estimada para una pieza."""
    nota_estimada = 1
    
    # Sumar 1 si la tolerancia es 1
    if tolerancia == 1:
        nota_estimada += 1

    # Sumar 1 si las operaciones son 1
    if operaciones == 1:
        nota_estimada += 1
    
    # Sumar 1 si el volumen está fuera del rango permitido
    if volumen > 274625 or (volumen < 1000 and material != 'ALUMINIO'):
        nota_estimada += 1
    elif volumen > 318500 or volumen < 1000:
        nota_estimada += 1
    
    # Sumar 2 si se cumplen ambas condiciones
    if tolerancia == 1 and (volumen > 274625 or volumen < 1000):
        nota_estimada += 1  
    elif operaciones == 1 and (volumen > 274625 or volumen < 1000):
        nota_estimada += 1  
    
    return nota_estimada
