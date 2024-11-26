from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

def evaluate_model(model, X_test, y_test):
    """Evalúa el modelo con el conjunto de prueba y genera métricas."""
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"MSE: {mse:.2f}, R2: {r2:.2f}")
    
    plt.figure(figsize=(8, 6))
    plt.plot(y_test.values, label="Real", marker='o')
    plt.plot(y_pred, label="Predicción", marker='x')
    plt.title("Comparación entre valores reales y predichos")
    plt.xlabel("Índice")
    plt.ylabel("Valores")
    plt.legend()
    plt.show()
    return mse, r2
