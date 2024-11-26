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

def remove_outliers(df, column_list=None):
    """
    Elimina outliers de las columnas numéricas seleccionadas usando el método IQR.
    :param df: DataFrame con los datos.
    :param column_list: Lista de columnas donde buscar outliers. Si es None, se procesan todas las columnas numéricas.
    :return: DataFrame limpio y un DataFrame con los outliers eliminados.
    """
    if column_list is None:
        column_list = df.select_dtypes(include=['float64', 'int64']).columns

    df_cleaned = df.copy()
    outliers = pd.DataFrame()

    for column in column_list:
        if column not in df_cleaned.columns:
            continue

        q1 = df_cleaned[column].quantile(0.25)
        q3 = df_cleaned[column].quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers_in_column = df_cleaned[(df_cleaned[column] < lower_bound) | (df_cleaned[column] > upper_bound)]
        outliers = pd.concat([outliers, outliers_in_column])

        # Eliminar outliers de la columna
        df_cleaned = df_cleaned[(df_cleaned[column] >= lower_bound) & (df_cleaned[column] <= upper_bound)]

    return df_cleaned, outliers
