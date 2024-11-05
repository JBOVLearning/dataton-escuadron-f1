import pandas as pd
import matplotlib.pyplot as plt

df_vacantes = pd.read_csv('data/DATA_VACANTES.csv', low_memory=False)

print(df_vacantes.shape[0]) # 72582

print(df_vacantes.isnull().sum())

# Si se borra los datos nulos, se pierden 24051 registros asi que se decide no borrarlos
# df_vacantes = df_vacantes.dropna()

# print(df_vacantes.shape[0]) # 48531

# print(df_vacantes.isnull().sum())

# Index([
#   'ID', 
#   'NOMBREAVISO' (Nombre del aviso de oferta laboral), 
#   'VACANTES' (Cantidad de vacantes), 
#   'POSTULANTES' (Cantidad de personas que han postulado (actualizado al 17/10/2024)), 
#   'IDEMPRESA' (Identificador de la empresa anonimizado), 
#   'UBIGEO' (Codigo de ubicacion geográfica donde se realizará el trabajo), 
#   'DEPARTAMENTO' (DEPARTAMENTO donde se realizará el trabajo.), 
#   'PROVINCIA' (PROVINCIA donde se realizará el trabajo.), 
#   'DISTRITO' (DISTRITO donde se realizará el trabajo.), 
#   'FECHAINICIO' (Fecha de inicio de publicación de aviso de oferta de empleo), 
#   'FECHAFIN' (Fecha fin de publicación de aviso de oferta de empleo), 
#   'SINEXPERIENCIA' (Si el puesto requiere experiencia = NO , si no requiere experiencia = SI), 
#   'MODALIDADTRABAJO' (Modalidad de trabajo : 1 = Remoto, 2 = Presencial, 3 = Mixto), 
#   'TIEMPOEXPERIENCIA' (Tiempo de experiencia que se solicita que tenga el postulante), 
#   'TIPOTIEMPOEXPERIENCIA' (Unidades de medidas de tiempo de experiencia), 
#   'SECTOR' (Sector industrial a la que pertenece la empresa), 
#   'ESCO' (Clasificador ocupacional de la vacante), 
#   'ESPCD' (Es una vacante para personas con discapacidad (SI, NO)),
#   'FECHACREACION' (Fecha de registro de vacante en la Plataforma Bolsa de Trabajo), 
#   'ACTIVO' (Estado de vacante: Activo = Vacante vigente, En Espera = xxxxxx)
#   ], 
#   dtype='object')

from colores import colores

# ========================================== Analisis ==========================================

# 1. ¿Cuántas vacantes hay para personas con discapacidad?
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

plt.suptitle("Análisis de vacantes para personas con discapacidad", fontsize=16)
si_discapacitados = df_vacantes[df_vacantes['ESPCD'] == 'SI'].shape[0]
no_discapacitados = df_vacantes[df_vacantes['ESPCD'] == 'NO'].shape[0]
titulos = ['Discapacitados', 'No Discapacitados']
arrays = [si_discapacitados, no_discapacitados]

axs[0].pie(arrays, labels=titulos, autopct='%1.1f%%', startangle=140, colors=[colores[0], colores[1]])
axs[1].bar(titulos, arrays, color=[colores[0], colores[1]])

plt.tight_layout()
plt.show()

# 2. ¿Cuántas vacantes hay para personas discapacitadas con y sin experiencia?
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

plt.suptitle("Análisis de vacantes para personas con discapacidad con y sin experiencia", fontsize=16)

si_discapacitados = df_vacantes[(df_vacantes['ESPCD'] == 'SI') & (df_vacantes['SINEXPERIENCIA'] == 'SI')].shape[0]
no_discapacitados = df_vacantes[(df_vacantes['ESPCD'] == 'SI') & (df_vacantes['SINEXPERIENCIA'] == 'NO')].shape[0]
no_precisa = df_vacantes[(df_vacantes['ESPCD'] == 'SI') & (df_vacantes['SINEXPERIENCIA'] == 'No precisa')].shape[0]

total_vacantes = si_discapacitados + no_discapacitados + no_precisa
titulos = ['Con Experiencia', 'Sin Experiencia', 'No Precisa']
arrays = [si_discapacitados, no_discapacitados, no_precisa]
colores.append('#FFA07A')

axs[0].pie(arrays, labels=titulos, autopct='%1.1f%%', startangle=140, colors=[colores[0], colores[1], colores[2]])
axs[1].bar(titulos, arrays, color=[colores[0], colores[1], colores[2]])

plt.tight_layout()
plt.show()

# 3. ¿Cuántas vacantes hay por ubicación geográfica (departamento, provincia, distrito)?
fig, axs = plt.subplots(2, 2, figsize=(12, 10))  

plt.suptitle("Análisis de vacantes por ubicación geográfica", fontsize=16)

departamento = df_vacantes['DEPARTAMENTO'].value_counts().head(10)
provincia = df_vacantes['PROVINCIA'].value_counts().head(10)
distrito = df_vacantes['DISTRITO'].value_counts().head(10)

axs[0, 0].bar(departamento.index, departamento.values, color=colores[0])
axs[0, 0].set_title("Departamento")
plt.setp(axs[0, 0].xaxis.get_majorticklabels(), rotation=45)

axs[0, 1].bar(provincia.index, provincia.values, color=colores[1])
axs[0, 1].set_title("Provincia")
plt.setp(axs[0, 1].xaxis.get_majorticklabels(), rotation=45)

axs[1, 0].bar(distrito.index, distrito.values, color=colores[2])
axs[1, 0].set_title("Distrito")
plt.setp(axs[1, 0].xaxis.get_majorticklabels(), rotation=45)

axs[1, 1].axis('off')

plt.tight_layout()
plt.show()

# 4. Dentro de las vacantes de trabajo para discapacitados, ver qué tipo de modalidad de trabajo se solicita frecuentemente.
vacantes_discapacitados = df_vacantes[df_vacantes['ESPCD'] == 'SI']
modalidades = vacantes_discapacitados['MODALIDADTRABAJO'].value_counts()
plt.figure(figsize=(10, 6))
modalidades.plot(kind='bar', color=colores[0])
plt.title("Modalidades de trabajo solicitadas para discapacitados", fontsize=16)
plt.tight_layout()
plt.show()

# 5. Frecuencia del número de vacantes que se pide en cada aviso laboral 
plt.figure(figsize=(10, 6))
df_vacantes['VACANTES'].hist(bins=10, color=colores[0], edgecolor='black')
plt.title("Frecuencia de Vacantes solicitadas en cada aviso laboral", fontsize=16)
plt.tight_layout()
plt.show()

# 6. ¿Cuántas vacantes hay por tipo de unidad de medida de tiempo de experiencia?
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

plt.suptitle("Análisis de vacantes según tipo de unidad de medida de experiencia", fontsize=16)

tipo_experiencia_count = df_vacantes['TIPOTIEMPOEXPERIENCIA'].value_counts()

axs[0].pie(tipo_experiencia_count.values, labels=tipo_experiencia_count.index, autopct='%1.1f%%', startangle=140, colors=colores[:len(tipo_experiencia_count)])

axs[1].bar(tipo_experiencia_count.index, tipo_experiencia_count.values, color=colores[:len(tipo_experiencia_count)])
plt.setp(axs[1].xaxis.get_majorticklabels(), rotation=45)

plt.tight_layout()
plt.show()

# 7. ¿Cuántas vacantes hay por sector industrial?
fig, axs = plt.subplots(1, 2, figsize=(16, 10))

plt.suptitle("Análisis de vacantes por sector industrial", fontsize=16)

sector_count = df_vacantes['SECTOR'].value_counts().head(10)

axs[0].pie(sector_count.values, labels=sector_count.index, autopct='%1.1f%%', startangle=140, colors=colores[:len(sector_count)])
axs[1].bar(sector_count.index, sector_count.values, color=colores[:len(sector_count)])
plt.setp(axs[1].xaxis.get_majorticklabels(), rotation=45)

plt.tight_layout()
plt.show()

# 8. Vacantes para personas con discapacidad según sector industrial
vacantes_discapacitados = df_vacantes[df_vacantes['ESPCD'] == 'SI']
sector_discapacitados = vacantes_discapacitados['SECTOR'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sector_discapacitados.plot(kind='bar', color=colores[0])
plt.title("Sectores con más vacantes para personas con discapacidad", fontsize=16)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()