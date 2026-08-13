import pandas as pd
import numpy as np

def remove_negative_values(df, Column):
    # Optimizado: Cambiamos .apply(lambda) por .loc que es mucho más rápido y automático
    df.loc[df[Column] < 0, Column] = np.nan
    return df

def replace_outliers_with_zscore(df, Column, threshold=2):
    z_scores = (df[Column] - df[Column].mean()) / df[Column].std()
    df[Column] = df[Column].mask((z_scores > threshold) | (z_scores < -threshold), df[Column].mean())
    return df

def map_column_values(df, column, mapping_dict):
    df[column] = df[column].apply(
        lambda value: mapping_dict.get(str(value).lower().strip(), np.nan) if not pd.isna(value) else np.nan
    )
    return df

def fill_na_in_column(df, column, value):
    # Si el valor que pasamos es el string "mean", calculamos la media real y limpia de ese momento
    if value == "mean":
        value = df[column].mean()
    df[column] = df[column].fillna(value)
    return df

def preprocess_data(df):
    # REGLA: Todas las llaves en minúsculas debido al .lower() de tu función
    education_mapping = {
        'bacherlors': 'Bachelor',
        'bachelors': 'Bachelor', # Agregado por si viene en inglés bien escrito
        'master': 'Master',
        'phd': 'PhD',
        'no education': 'NE'
    }

    gender_mapping = {
        'm': 'M',
        'f': 'F',
        'masculino': 'M', # Agregados comunes para mayor automatización
        'femenino': 'F'
    }

    return (
        df.pipe(remove_negative_values, "Edad")
        .pipe(remove_negative_values, "Ingresos")
        .pipe(remove_negative_values, "Hijos")
        
        .pipe(replace_outliers_with_zscore, "Edad")
        .pipe(replace_outliers_with_zscore, "Ingresos")
        .pipe(replace_outliers_with_zscore, "Hijos")
        .pipe(replace_outliers_with_zscore, "Altura")
        
        .pipe(map_column_values, 'Nivel_Educación', education_mapping)
        .pipe(map_column_values, 'Género', gender_mapping)
        
        .pipe(fill_na_in_column, 'Ciudad', "Desconocido")
        .pipe(fill_na_in_column, 'Género', "Desconocido")
        
        # Al pasar "mean", el método dinámico calcula el promedio correcto post-limpieza
        .pipe(fill_na_in_column, 'Edad', "mean") 
        .pipe(fill_na_in_column, 'Ingresos', "mean")
        .pipe(fill_na_in_column, 'Hijos', "mean")
        .pipe(fill_na_in_column, 'Altura', "mean")
        .pipe(fill_na_in_column, 'Nivel_Educación', "NE")
    )

# --- EJECUCIÓN ---
df = pd.read_csv(r'C:\Users\maico\OneDrive\Desktop\ANALISIS DE DATOS CODES\machinlearning\dataset_1.csv', index_col=0)
df = preprocess_data(df)

# EXTRAER EL ARCHIVO AUTOMÁTICAMENTE
df.to_csv(r'C:\Users\maico\OneDrive\Desktop\ANALISIS DE DATOS CODES\machinlearning\dataset_1_limpio.csv', index=False, encoding='utf-8-sig')
print("✅ ¡Procesamiento y extracción completada con éxito!")