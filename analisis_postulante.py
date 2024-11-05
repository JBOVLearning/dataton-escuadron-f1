import pandas as pd
import matplotlib.pyplot as plt

df_postulante = pd.read_csv('data/DATA_POSTULANTE.csv')
 
print(df_postulante.shape[0]) # 2715

print(df_postulante.isnull().sum())

# Si se borra los datos nulos, se pierden 10 registros asi que se decide borrarlos ya que no afecta mucho al análisis
df_postulante = df_postulante.dropna()

print(df_postulante.shape[0]) # 2705

print(df_postulante.isnull().sum())

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

from colores import colores

# ========================================== Análisis ==========================================

# 1. Distribución de postulantes por sexo
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

plt.suptitle("Análisis de postulantes por sexo", fontsize=16)
sexo_femenino = df_postulante[df_postulante['SEXO'] == 'F'].shape[0]
sexo_masculino = df_postulante[df_postulante['SEXO'] == 'M'].shape[0]
titulos = ['Femenino', 'Masculino']
arrays = [sexo_femenino, sexo_masculino]

axs[0].pie(arrays, labels=titulos, autopct='%1.1f%%', startangle=140, colors=[colores[0], colores[1]])
axs[1].bar(titulos, arrays, color=[colores[0], colores[1]])

plt.tight_layout()
plt.show()

# 2. Distribución de edad de los postulantes
plt.figure(figsize=(10, 6))
df_postulante['EDAD'].hist(bins=20, color=colores[0], edgecolor='black')
plt.title("Distribución de Edad de los Postulantes", fontsize=16)
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()

# 3. Análisis de postulantes por ubicación geográfica (departamento, provincia, distrito)
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

plt.suptitle("Análisis de postulantes por ubicación geográfica", fontsize=16)

departamento = df_postulante['DEPARTAMENTO'].value_counts().head(5)
provincia = df_postulante['PROVINCIA'].value_counts().head(5)
distrito = df_postulante['DISTRITO'].value_counts().head(5)

axs[0, 0].bar(departamento.index, departamento.values, color=colores[:len(departamento)])
axs[0, 0].set_title("Departamento")
plt.setp(axs[0, 0].xaxis.get_majorticklabels(), rotation=45)

axs[0, 1].bar(provincia.index, provincia.values, color=colores[:len(provincia)])
axs[0, 1].set_title("Provincia")
plt.setp(axs[0, 1].xaxis.get_majorticklabels(), rotation=45)

axs[1, 0].bar(distrito.index, distrito.values, color=colores[:len(distrito)])
axs[1, 0].set_title("Distrito")
plt.setp(axs[1, 0].xaxis.get_majorticklabels(), rotation=45)

axs[1, 1].axis('off')

plt.tight_layout()
plt.show()

# 4. Distribución de postulantes inscritos en CONADIS
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

plt.suptitle("Análisis de postulantes inscritos en CONADIS", fontsize=16)
conadis_si = df_postulante[df_postulante['ESTADO_CONADIS'] == 1].shape[0]
conadis_no = df_postulante[df_postulante['ESTADO_CONADIS'] == 0].shape[0]
titulos = ['Inscritos en CONADIS', 'No Inscritos en CONADIS']
arrays = [conadis_si, conadis_no]

axs[0].pie(arrays, labels=titulos, autopct='%1.1f%%', startangle=140, colors=[colores[0], colores[1]])
axs[1].bar(titulos, arrays, color=[colores[0], colores[1]])

plt.tight_layout()
plt.show()