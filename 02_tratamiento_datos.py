
import pandas as pd
import numpy as np



def remove_negative_values(df, Column):
    df[Column] = df[Column].apply(lambda x: np.nan if x < 0 else x)
    return df
    

def replace_outliers_with_zscore(df, Column, threshold=2):

    z_scores = (df[Column] - df[Column].mean()) / df[Column].std()
    df[Column] = df[Column].mask((z_scores > threshold) | (z_scores < -threshold), df[Column].mean())
    return df


def map_column_values(df, column, mapping_dict):
    # Condición segura: si el valor es nulo, déjalo nulo. Si es texto, límpialo y búscalo en el diccionario.
    df[column] = df[column].apply(
        lambda value: mapping_dict.get(str(value).lower().strip(), np.nan) if not pd.isna(value) else np.nan
    )
    return df

def fill_na_in_column(df, column, value):
    df[column] = df[column].fillna(value)
    return df


def preprocess_data(df):
    education_mapping = {
    'Bacherlors': 'Bachelor',
    'master': 'Master',
    'pHd': 'PhD',
    'no education': 'NE',
    'NaN': 'NE'
    }

    gender_mapping = {
    'm': 'M',
    'f': 'F'
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
    .pipe(fill_na_in_column, 'Edad', df['Edad'].mean()) 
    .pipe(fill_na_in_column, 'Ingresos', df['Ingresos'].mean())
    .pipe(fill_na_in_column, 'Hijos', df['Hijos'].mean())
    .pipe(fill_na_in_column, 'Altura', df['Altura'].mean())
    .pipe(fill_na_in_column, 'Nivel_Educación', "NE")

    )


df = pd.read_csv(r'C:\Users\maico\OneDrive\Desktop\ANALISIS DE DATOS CODES\machinlearning\dataset_1.csv', index_col=0)

df = preprocess_data(df)    

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())