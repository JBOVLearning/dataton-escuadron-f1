import pandas as pd
import matplotlib.pyplot as plt

df_postulante = pd.read_csv('data/DATA_POSTULANTE.csv')

# Index([
#   'ID_POSTULANTE' (Código o llave para relacionarlo con el archivo de DATA_EDUCACION, DATA_EXPERIENCIASLABORALES. ID del postulante Anonimizado),
#   'EDAD' (Edad del postulante),
#   'SEXO' (Sexo del postulante. F = Femenino, M = Masculino),
#   'DEPARTAMENTO' (Departamento donde vive el postulante),
#   'PROVINCIA' (Provincia  donde vive el postulante),
#   'DISTRITO' (Distrito  donde vive el postulante),
#   'UBIGEO' (Codigo de ubicacion geografica donde vive el postulante),
#   'ESTADO_CONADIS' (Inscrito en CONADIS; 1 = Si esta Inscrito, 0 = No esta incrito),
#   'DOC_ID' (Código o llave para relacionarlo con el archivo de DATA_DISCAPACIDAD)
#   ], 
#   dtype='object')