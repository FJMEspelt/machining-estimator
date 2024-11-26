import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(df, title="Histogramas"):
    """Genera histogramas para todas las columnas numéricas del DataFrame."""
    df.hist(bins=20, figsize=(12, 8), color='skyblue', edgecolor='black')
    plt.suptitle(title, fontsize=16)
    plt.show()

def plot_correlation_heatmap(df, title="Mapa de Correlación"):
    """Genera un mapa de calor para mostrar correlaciones entre columnas numéricas."""
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title(title, fontsize=16)
    plt.show()
