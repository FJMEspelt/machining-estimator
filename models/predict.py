import pandas as pd

def predict_new_data(model, new_data, X_columns):
    """Realiza predicciones con el modelo."""
    new_data_prepared = pd.get_dummies(new_data, drop_first=True)
    for col in X_columns:
        if col not in new_data_prepared.columns:
            new_data_prepared[col] = 0
    new_data_prepared = new_data_prepared[X_columns]
    return model.predict(new_data_prepared)
