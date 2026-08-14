import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

class PipelineProcesamiento(BaseEstimator, TransformerMixin):
    def __init__(self):
        # Aquí guardamos los diccionarios fijos
        self.education_mapping = {'bacherlors': 'Bachelor', 'bachelors': 'Bachelor', 'master': 'Master', 'phd': 'PhD', 'no education': 'NE'}
        self.gender_mapping = {'m': 'M', 'f': 'F', 'masculino': 'M', 'femenino': 'F'}
        
        # 🧠 AQUÍ SE GUARDARÁN LOS PROMEDIOS APRENDIDOS EN EL FIT
        self.medias_ = {}
        self.stds_ = {} 

    def fit(self, X, y=None):
        X_temp = X.copy()
        columnas_num = ["Edad", "Ingresos", "Hijos", "Altura"]
        
        for col in columnas_num:
            # Paso 1: Quitar los negativos temporalmente
            clean_series = X_temp[col].mask(X_temp[col] < 0)
            
            # Paso 2: Calcular un Z-Score temporal para detectar outliers
            mean_inicial = clean_series.mean()
            std_inicial = clean_series.std()
            
            if std_inicial > 0:
                z_scores_temp = (clean_series - mean_inicial) / std_inicial
                # Filtramos: dejamos solo lo que NO sea outlier (entre -2 y 2)
                sin_outliers = clean_series.mask((z_scores_temp > 2) | (z_scores_temp < -2))
            else:
                sin_outliers = clean_series
                
            # Paso 3: ¡AQUÍ SÍ! Guardamos la media y std DEFINITIVAS, 100% limpias
            self.medias_[col] = sin_outliers.mean()
            self.stds_[col] = sin_outliers.std()
            
        return self

    def transform(self, X):
        # 2. El TRANSFORM aplica las reglas usando los promedios que ya aprendió el FIT
        df = X.copy()
        
        # Tratamiento de negativos
        for col in ["Edad", "Ingresos", "Hijos"]:
            df.loc[df[col] < 0, col] = np.nan
            
        # Reemplazo de outliers con Z-Score usando las medias e históricas aprendidas en el FIT
        for col in ["Edad", "Ingresos", "Hijos", "Altura"]:
            if self.stds_[col] > 0:
                z_scores = (df[col] - self.medias_[col]) / self.stds_[col]
                df[col] = df[col].mask((z_scores > 2) | (z_scores < -2), self.medias_[col])
                
        # Mapeo de texto seguro
        df['Nivel_Educación'] = df['Nivel_Educación'].apply(lambda v: self.education_mapping.get(str(v).lower().strip(), np.nan) if not pd.isna(v) else np.nan)
        df['Género'] = df['Género'].apply(lambda v: self.gender_mapping.get(str(v).lower().strip(), np.nan) if not pd.isna(v) else np.nan)
        
        # Rellenar Nulos Categóricos
        df['Ciudad'] = df['Ciudad'].fillna("Desconocido")
        df['Género'] = df['Género'].fillna("Desconocido")
        df['Nivel_Educación'] = df['Nivel_Educación'].fillna("NE")
        
        # Rellenar Nulos Numéricos usando las MEDIAS EXACTAS guardadas en el FIT
        for col in ["Edad", "Ingresos", "Hijos", "Altura"]:
            df[col] = df[col].fillna(self.medias_[col])


        # 🔥 NUEVO: AJUSTE DE TIPOS INTEGRADO ANTES DE RETORNAR El DF
        df['Edad'] = df['Edad'].round(0).astype('Int64')
        df['Ingresos'] = df['Ingresos'].round(0).astype('float64')
        df['Hijos'] = df['Hijos'].round(0).astype('Int64')
        df["Altura"] = df["Altura"].round(0).astype('float64')
            
            
        return df

    

# --- CÓMO SE EJECUTA AHORA ---
df_entrenamiento = pd.read_csv('dataset_1.csv', index_col=0)

# Inicializas tu automatizador
preprocesador = PipelineProcesamiento()

# EN UNA SOLA LÍNEA: Entrena (fit) y limpia (transform) tu dataset actual
df_limpio = preprocesador.fit_transform(df_entrenamiento)

# EXTRAER EL ARCHIVO AUTOMÁTICAMENTE
df_limpio.to_csv(r'C:\Users\maico\OneDrive\Desktop\ANALISIS DE DATOS CODES\machinlearning\dataset_1_limpiov4.csv', index=False, encoding='utf-8-sig')
print("✅ ¡Procesamiento y extracción completada con éxito!")

