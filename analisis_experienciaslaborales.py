import pandas as pd
import matplotlib.pyplot as plt

df_experienciaslaborales = pd.read_csv('data/DATA_EXPERIENCIASLABORALES.csv', delimiter=';')

# Index([
#   'ID_POSTULANTE' (Código o llave para relacionarlo con el archivo de DATA_POSTULANTE. Anonimizado),
#   'EMPRESA' (Nombre de la empresa donde laboró. Anonimizado),
#   'FECHAINICIO' (Fecha de inicio de labores),
#   'FECHAFIN' (Fin de la relacion laboral),
#   'DESCRIPCION' (Descripción de la experiencia),
#   'RANGO_SALARIAL' (Rango salarial)
#   ], 
#   dtype='object')