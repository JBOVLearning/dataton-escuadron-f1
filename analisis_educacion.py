import pandas as pd
import matplotlib.pyplot as plt

df_educacion = pd.read_csv('data/DATA_EDUCACION.csv', delimiter=';')

# print(df_educacion.shape[0]) # 292708

# Si se borra los datos nulos, se pierden 276159 registros asi que se decide no borrarlos
# print(df_educacion.isnull().sum())

# df_educacion = df_educacion.dropna()

# print(df_educacion.shape[0]) # 16549

# print(df_educacion.isnull().sum())

# Index([
#   'ID_POSTULANTE' (Código o llave para relacionarlo con el archivo de DATA_POSTULANTE),
#   'INSTITUCION' (Institución donde realizó el estudio),
#   'GRADO' (Grado académico),
#   'FECHAINICIO' (Fecha inicio de estudios),
#   'FECHAFIN' (Fecha fin de estudios),
#   'CARRERA' (Carrera que estudió)
#   ], 
#   dtype='object')

from colores import colores

# ========================================== Analisis ==========================================

# 1. Top 10 carreras mas comunes
carreras = df_educacion['CARRERA'].value_counts().head(10) 

fig, axs = plt.subplots(1, 2, figsize=(18, 8))
plt.suptitle("Análisis las 10 carreras más comunes elegidas por los postulantes", fontsize=16)

carreras.plot(kind='bar', color=colores[:len(carreras)], ax=axs[0])
axs[0].tick_params(axis='x', rotation=45)

carreras.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=colores[:len(carreras)], ax=axs[1])
axs[1].set_ylabel('') 

plt.tight_layout()
plt.show()

# 2. Top 10 instituciones mas afrecuentes
instituciones = df_educacion['INSTITUCION'].value_counts().head(10)

fig, axs = plt.subplots(1, 2, figsize=(18, 8))
plt.suptitle("Análisis de las 10 instituciones más frecuentes", fontsize=16)

instituciones.plot(kind='bar', color=colores[:len(instituciones)], ax=axs[0])
axs[0].tick_params(axis='x', rotation=45)

instituciones.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=colores[:len(instituciones)], ax=axs[1])
axs[1].set_ylabel('')
plt.tight_layout()
plt.show()
