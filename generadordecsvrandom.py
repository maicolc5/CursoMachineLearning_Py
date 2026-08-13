import pandas as pd
import numpy as np

# Configurar aleatoriedad
np.random.seed(42)
n_filas = 100

# Generar datos aleatorios estructurados
data = {
    'Edad': np.random.choice([25, 34, 45, -5, 120, np.nan], size=n_filas, p=[0.3, 0.3, 0.2, 0.05, 0.05, 0.1]),
    'Ingresos': np.random.choice([2000, 3500, 5000, -1000, 95000, np.nan], size=n_filas, p=[0.3, 0.3, 0.2, 0.05, 0.05, 0.1]),
    'Hijos': np.random.choice([0, 1, 2, -1, np.nan], size=n_filas, p=[0.4, 0.3, 0.1, 0.1, 0.1]),
    'Altura': np.random.choice([1.65, 1.75, 1.80, 3.50, np.nan], size=n_filas, p=[0.4, 0.3, 0.2, 0.05, 0.05]),
    'Género': np.random.choice(['m', 'f', 'Masculino', 'Femenino', np.nan], size=n_filas, p=[0.3, 0.3, 0.1, 0.1, 0.2]),
    'Ciudad': np.random.choice(['Madrid', 'Barcelona', 'Valencia', np.nan], size=n_filas, p=[0.4, 0.3, 0.2, 0.1]),
    'Nivel_Educación': np.random.choice(['Bacherlors', 'master', 'pHd', 'no education', np.nan], size=n_filas, p=[0.3, 0.3, 0.2, 0.1, 0.1])
}

# Crear DataFrame y guardar
df_random = pd.DataFrame(data)
df_random.index.name = 'id'
df_random.to_csv('dataset_1_random.csv')
print("✅ Archivo 'dataset_1_random.csv' generado con éxito para pruebas.")