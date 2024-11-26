from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def train_model(X, y, model_name):
    """Entrena un modelo seleccionado."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if model_name == 'linear_regression':
        model = LinearRegression()
    elif model_name == 'random_forest':
        model = RandomForestRegressor(n_estimators=100, random_state=42)
    elif model_name == 'svm':
        model = SVR(kernel='rbf')
    else:
        raise ValueError("Modelo no válido seleccionado.")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    return model, {"mse": mse, "r2": r2}
