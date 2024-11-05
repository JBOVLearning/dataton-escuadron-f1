import pandas as pd
import matplotlib.pyplot as plt

df_experienciaslaborales = pd.read_csv('data/DATA_EXPERIENCIASLABORALES.csv', delimiter=';')

print(df_experienciaslaborales.shape[0]) # 599640

print(df_experienciaslaborales.isnull().sum())

# Si se borra los datos nulos, se pierden 388044 registros asi que se decide no borrarlos
# df_experienciaslaborales = df_experienciaslaborales.dropna()

# print(df_experienciaslaborales.shape[0]) #211596

# print(df_experienciaslaborales.isnull().sum())

# Index([
#   'ID_POSTULANTE' (Código o llave para relacionarlo con el archivo de DATA_POSTULANTE. Anonimizado),
#   'EMPRESA' (Nombre de la empresa donde laboró. Anonimizado),
#   'FECHAINICIO' (Fecha de inicio de labores),
#   'FECHAFIN' (Fin de la relacion laboral),
#   'DESCRIPCION' (Descripción de la experiencia),
#   'RANGO_SALARIAL' (Rango salarial)
#   ], 
#   dtype='object')

from colores import colores

# ========================================== Analisis ==========================================

# 1. ¿Cuál es la frecuencia de cada rango salarial?
plt.figure(figsize=(10, 6))
rango_salarial_count = df_experienciaslaborales['RANGO_SALARIAL'].value_counts().sort_index()

# Crear un gráfico de barras
rango_salarial_count.plot(kind='bar', color=colores[:len(rango_salarial_count)], edgecolor='black')
plt.title('Distribución de rangos salariales', fontsize=16)
plt.xlabel('Rango Salarial', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
