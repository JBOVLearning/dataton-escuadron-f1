import pandas as pd
import matplotlib.pyplot as plt

# Cargamos los datasets
df_discapacidad = pd.read_csv('data/DATA_DISCAPACIDAD.csv')

# Index([
#   'DBIDPOSTULANTE' (ID POSTULANTE, llave foránea la cual sirve para unir este dataset con el dataset de POSTULANTES), 
#   'CAUSA' (Causa de la discapacidad), 
#   'DSCORE' (1= Sin dificultad, 2 = Dificultad leve o moderada, 3 = Dificultad severa)
#   ], 
#   dtype='object')

# 1. Distribucion de causas de discapacidad en los postulantes
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
df_discapacitado['CAUSA'].hist(bins=20, edgecolor='black')
plt.title("Distribucion de causas de discapacidad en los postulantes", fontsize=16)
plt.xlabel("Causas")
plt.ylabel("Cantidad")
plt.show()

#2. Distribucion de la dificultad que causaria la discapacidad
plt.figure(figsize=(10, 6))
df_discapacitado['DSCORE'].hist(bins=20, edgecolor='black')
plt.title("Distribucion de la dificultad que causaria la discapacidad", fontsize=16)
plt.xlabel("1= Sin dificultad, 2 = Dificultad leve o moderada, 3 = Dificultad severa")
plt.ylabel("Cantidad")
plt.show()
