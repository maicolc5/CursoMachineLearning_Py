import pandas as pd
# 🚀 Importas tu clase desde tu otro archivo .py
from limpiadores import PipelineProcesamiento 

# 1. Cargas un dataset completamente nuevo y sucio
df_nuevos_clientes = pd.read_csv('dataset_1_random.csv')

# 2. Inicializas el preprocesador
preprocesador = PipelineProcesamiento()

# 3. EN UNA SOLA LÍNEA limpias absolutamente todo usando las reglas guardadas
df_listo = preprocesador.fit_transform(df_nuevos_clientes)