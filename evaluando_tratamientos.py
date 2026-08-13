


import pandas as pd
import numpy as np


df1 = pd.read_csv(r'C:\Users\maico\OneDrive\Desktop\ANALISIS DE DATOS CODES\machinlearning\dataset_1_limpio.csv', index_col=0)

df2 = pd.read_csv(r'C:\Users\maico\OneDrive\Desktop\ANALISIS DE DATOS CODES\machinlearning\dataset_1_limpiov2.csv', index_col=0)

df3 = pd.read_csv(r'C:\Users\maico\OneDrive\Desktop\ANALISIS DE DATOS CODES\machinlearning\dataset_1_limpiov3.csv', index_col=0)

df4 = pd.read_csv(r'C:\Users\maico\OneDrive\Desktop\ANALISIS DE DATOS CODES\machinlearning\dataset_1_limpiov4.csv', index_col=0)



desc1 = df1.describe()
desc2 = df2.describe()
desc3 = df3.describe()
desc4 = df4.describe()

# 3. Crear el archivo Excel único y escribir cada describe en una pestaña
with pd.ExcelWriter('resumenes_combinados.xlsx', engine='openpyxl') as writer:
    desc1.to_excel(writer, sheet_name='Resumen_Archivo1', index=True)
    desc2.to_excel(writer, sheet_name='Resumen_Archivo2', index=True)
    desc3.to_excel(writer, sheet_name='Resumen_Archivo3', index=True)
    desc4.to_excel(writer, sheet_name='Resumen_Archivo4', index=True)