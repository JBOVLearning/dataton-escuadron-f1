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