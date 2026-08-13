


import pandas as pd
import numpy as np


df = pd.read_csv(r'C:\Users\maico\OneDrive\Desktop\ANALISIS DE DATOS CODES\machinlearning\dataset_1.csv', index_col=0)

#print(df.head())
#print(df.shape)
#print(df.info())
#print(df.describe())

set_gen = set(df['Género'].to_list())
set_edu = set(df['Nivel_Educación'].to_list())
set_ciu = set(df['Ciudad'].to_list())

#print(set_gen)
#print(set_edu)
#print(set_ciu)      

# 1 Tratamiento de valores negativos (Forma rápida y eficiente)
for column in ['Edad', 'Ingresos', 'Hijos']:
    df.loc[df[column] < 0, column] = np.nan

# 2 Imputar valores faltantes (Asignando directamente sin inplace)
for column in ['Edad', 'Ingresos', 'Hijos']:
    df[column] = df[column].fillna(df[column].mean())

for column in ['Género', 'Ciudad']:
    df[column] = df[column].fillna(df[column].mode()[0])

# 3 Mapeo de datos

education_mapping = {
    'Bacherlors': 'Bachelor',
    'master': 'Master',
    'pHd': 'PhD',
    'no education': 'NE'
}

# Solo corrige los errores y respeta los que ya están bien
df['Nivel_Educación'] = df['Nivel_Educación'].replace(education_mapping)

# Al final, rellena los que venían vacíos de origen
df['Nivel_Educación'] = df['Nivel_Educación'].fillna('NE')



#OJO ESTA ES UNA ALTERNATIVA PERO DEBERIA DEFINIR TODOS MIS VALORES DENTRO DE EDUCATION_MAPPING DEBIDO A QUE LA FUNCION MAP REMPLAZA TODOS LOS VALORES NO SOLO LOS ERRONEOS
#df['Nivel_Educación'] = df['Nivel_Educación'].map(education_mapping).fillna('NE')


# Casteo de tipos

df['Edad'] = df['Edad'].astype('int64')
df['Ingresos'] = df['Ingresos'].astype('float64')
df['Hijos'] = df['Hijos'].astype('int64')
df["Altura"] = df["Altura"].astype('float64')

# COMPRUEBO QUE NO HAY VALORES NULOS
nulos_por_columna = df.isna().sum().loc[lambda x: x > 0]

if nulos_por_columna.empty:
    print("✅ ¡Perfecto! No hay valores nulos en ninguna columna del dataset.")
else:
    print("⚠️ Se encontraron las siguientes columnas con valores nulos:")
    print(nulos_por_columna)

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

#df.to_csv('dataset_procesado.csv', index=False)

