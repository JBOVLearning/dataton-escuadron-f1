import pandas as pd
import matplotlib.pyplot as plt

df_competencias = pd.read_csv('data/DATA_COMPETENCIAS.csv')

# Index([
#   'AVISOID' (Código o llave foránea, la cual sirtve para unir este dataset con el dataset de VACANTES), 
#   'NOMBRECOMPETENCIA' (Competencias requeridas para el puesto de trabajo)
#   ],  
#   dtype='object')