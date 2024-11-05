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

df_educacion = pd.read_csv('DATA_EDUCACION.csv', delimiter=';')

carreras = df_educacion['CARRERA'].value_counts().head(10)  # Mostrar solo las 10 más comunes

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
carreras.plot(kind='bar', color='orchid')
plt.title('Carreras más estudiadas (Top 10)')
plt.xlabel('Carrera')
plt.ylabel('Cantidad de postulantes')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
