import pandas as pd
import matplotlib.pyplot as plt

df_competencias = pd.read_csv('data/DATA_COMPETENCIAS.csv')

print (df_competencias.shape[0]) # 390748

# No hay datos nulos
print(df_competencias.isnull().sum())

# Index([
#   'AVISOID' (Código o llave foránea, la cual sirtve para unir este dataset con el dataset de VACANTES), 
#   'NOMBRECOMPETENCIA' (Competencias requeridas para el puesto de trabajo)
#   ],  
#   dtype='object')

from colores import colores

# ========================================== Analisis ==========================================

# 1. 10 competencias más requeridas
competencias = df_competencias['NOMBRECOMPETENCIA'].value_counts().head(10)

fig, axs = plt.subplots(1, 2, figsize=(16, 6))

plt.suptitle('Análisis de competencias más requeridas en las vacantes', fontsize=16)

axs[0].bar(competencias.index, competencias.values, color=colores[:len(competencias)], edgecolor='black')
axs[0].tick_params(axis='x', rotation=45)

axs[1].pie(competencias.values, labels=competencias.index, autopct='%1.1f%%', startangle=140, colors=colores[:len(competencias)])
axs[1].set_title('')

plt.tight_layout()
plt.show()
