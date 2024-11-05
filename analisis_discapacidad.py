import pandas as pd
import matplotlib.pyplot as plt

df_discapacidad = pd.read_csv('data/DATA_DISCAPACIDAD.csv')

print(df_discapacidad.shape[0]) # 62525

# No hay datos nulos
print(df_discapacidad.isnull().sum())

# Index([
#   'DBIDPOSTULANTE' (ID POSTULANTE, llave foránea la cual sirve para unir este dataset con el dataset de POSTULANTES), 
#   'CAUSA' (Causa de la discapacidad), 
#   'DSCORE' (1= Sin dificultad, 2 = Dificultad leve o moderada, 3 = Dificultad severa)
#   ], 
#   dtype='object')

from colores import colores

# ========================================== Analisis ==========================================

# 1. Distribución de Causas de la Discapacidad  
causas = df_discapacidad['CAUSA'].value_counts()

plt.figure(figsize=(10, 6))
causas.plot(kind='bar', color=colores[:len(causas)], edgecolor='black')
plt.title('Distribución de Causas de la Discapacidad', fontsize=16)
plt.xlabel('Causa de Discapacidad', fontsize=12)
plt.ylabel('Cantidad de Postulantes', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 2. Distribución de la Gravedad de la Discapacidad (DSCORE)
gravedad = df_discapacidad['DSCORE'].value_counts().sort_index()

fig, axs = plt.subplots(1, 2, figsize=(18, 8))

plt.suptitle("Gravedad de la Discapacidad (1=Sin dificultad, 2=Levele/Moderada, 3=Severa)", fontsize=16)

gravedad.plot(kind='bar', color=colores[:len(gravedad)], edgecolor='black', ax=axs[0])
axs[0].set_ylabel('Cantidad de Postulantes', fontsize=12)
axs[0].tick_params(axis='x', rotation=0)

gravedad.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=colores[:len(gravedad)], ax=axs[1])
axs[1].set_ylabel('')

plt.tight_layout()
plt.show()
