import os
import matplotlib.pyplot as plt
import seaborn as sns

def create_charts(df_preprocessed, output_dir="static/charts"):
    """Genera gráficos necesarios."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    numeric_df = df_preprocessed.select_dtypes(include=['float64', 'int64'])
    correlation_chart_path = os.path.join(output_dir, "correlation_matrix.png")
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.savefig(correlation_chart_path)
    plt.close()

    comparison_chart_path = os.path.join(output_dir, "note_vs_difficulty_comparison_colored.png")
    mae = (df_preprocessed['nota_estimada'] - df_preprocessed['Dificultad']).abs().mean()
    plt.figure(figsize=(12, 6))
    plt.scatter(range(len(df_preprocessed)), df_preprocessed['Dificultad'], color='blue')
    plt.scatter(range(len(df_preprocessed)), df_preprocessed['nota_estimada'], color='orange')
    plt.savefig(comparison_chart_path)
    plt.close()

    return {"correlation_matrix": correlation_chart_path, "note_vs_difficulty": comparison_chart_path}, mae
