import pandas as pd
import matplotlib.pyplot as plt

df_educacion = pd.read_csv('data/DATA_EDUCACION.csv', delimiter=';')

# Index([
#   'ID_POSTULANTE' (Código o llave para relacionarlo con el archivo de DATA_POSTULANTE),
#   'INSTITUCION' (Institución donde realizó el estudio),
#   'GRADO' (Grado académico),
#   'FECHAINICIO' (Fecha inicio de estudios),
#   'FECHAFIN' (Fecha fin de estudios),
#   'CARRERA' (Carrera que estudió)
#   ], 
#   dtype='object')