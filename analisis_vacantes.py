import pandas as pd
import matplotlib.pyplot as plt

df_vacantes = pd.read_csv('data/DATA_VACANTES.csv', low_memory=False)

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

# ========================================== Analisis ==========================================

# 1. ¿Cuántas vacantes hay para personas con discapacidad?
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

plt.suptitle("Análisis de vacantes para personas con discapacidad", fontsize=16)
plt.text(0.5, 0.02, f'Total de Vacantes: {df_vacantes.shape[0]}', ha='center', fontsize=10, transform=plt.gcf().transFigure)

si_discapacitados = df_vacantes[df_vacantes['ESPCD'] == 'SI'].shape[0]
no_discapacitados = df_vacantes[df_vacantes['ESPCD'] == 'NO'].shape[0]
colores = ['#87CEEB', '#FFD700']
titulos = ['Discapacitados', 'No Discapacitados']
arrays = [si_discapacitados, no_discapacitados]

axs[0].pie(arrays, labels=titulos, autopct='%1.1f%%', startangle=140, colors=colores)
axs[1].bar(titulos, arrays, color=colores)

axs[0].set_ylabel("")
axs[1].set_ylabel("Número de vacantes")

plt.tight_layout()
plt.show()

# 2. ¿Cuántas vacantes hay para personas discapacitadas con y sin experiencia?
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

plt.suptitle("Análisis de vacantes para personas con discapacidad con y sin experiencia", fontsize=16)

si_discapacitados = df_vacantes[(df_vacantes['ESPCD'] == 'SI') & (df_vacantes['SINEXPERIENCIA'] == 'SI')].shape[0]
no_discapacitados = df_vacantes[(df_vacantes['ESPCD'] == 'SI') & (df_vacantes['SINEXPERIENCIA'] == 'NO')].shape[0]
no_precisa = df_vacantes[(df_vacantes['ESPCD'] == 'SI') & (df_vacantes['SINEXPERIENCIA'] == 'No precisa')].shape[0]

total_vacantes = si_discapacitados + no_discapacitados + no_precisa

plt.text(0.5, 0.02, f'Total de vacantes para discapacitados: {total_vacantes}', ha='center', fontsize=10, transform=plt.gcf().transFigure)

titulos = ['Con Experiencia', 'Sin Experiencia', 'No Precisa']
arrays = [si_discapacitados, no_discapacitados, no_precisa]
colores.append('#FFA07A')

axs[0].pie(arrays, labels=titulos, autopct='%1.1f%%', startangle=140, colors=colores)
axs[1].bar(titulos, arrays, color=colores)

axs[0].set_ylabel("")
axs[1].set_ylabel("Número de vacantes")

plt.tight_layout()
plt.show()

# 3. ¿Cuántas vacantes hay por ubicacion geofrafica (departamento, provincia, distrito)?
fig, axs = plt.subplots(2, 2, figsize=(12, 10))  

plt.suptitle("Análisis de vacantes por ubicación geográfica", fontsize=16)

departamento = df_vacantes['DEPARTAMENTO'].value_counts().head(10)
provincia = df_vacantes['PROVINCIA'].value_counts().head(10)
distrito = df_vacantes['DISTRITO'].value_counts().head(10)

axs[0, 0].bar(departamento.index, departamento.values, color='#87CEEB')
axs[0, 0].set_title("Departamento")
plt.setp(axs[0, 0].xaxis.get_majorticklabels(), rotation=45)

axs[0, 1].bar(provincia.index, provincia.values, color='#FFD700')
axs[0, 1].set_title("Provincia")
plt.setp(axs[0, 1].xaxis.get_majorticklabels(), rotation=45)

axs[1, 0].bar(distrito.index, distrito.values, color='#FFA07A')
axs[1, 0].set_title("Distrito")
plt.setp(axs[1, 0].xaxis.get_majorticklabels(), rotation=45)

axs[1, 1].axis('off')

plt.tight_layout()
plt.show()

# 4. Dentro de las vacantes de trabajo para discapacitados, ver que tipo de modalidad de trabajo se solicita frecuentemente.
vacantes_discapacitados = df_vacantes[df_vacantes['ESPCD'] == 'SI']
modalidades = vacantes_discapacitados['MODALIDADTRABAJO'].value_counts()
plt.figure(figsize=(10, 6))
modalidades.plot(kind='bar', color='#87CEEB')
plt.title("Modalidades de Trabajo solicitadas para Discapacitados", fontsize=16)
plt.xlabel("Modalidad de Trabajo", fontsize=12)
plt.ylabel("Número de Vacantes", fontsize=12)
plt.tight_layout()
plt.show()

# 5. Frecuencia del numero de vacantes que se pide en cada aviso laboral 

plt.figure(figsize=(10, 6))
df_vacantes['VACANTES'].hist(bins=20, color='#FFD700', edgecolor='black')  # Ajusta el número de bins según sea necesario
plt.title("Frecuencia de Vacantes solicitadas en cada aviso laboral", fontsize=16)
plt.xlabel("Número de Vacantes", fontsize=12)
plt.ylabel("Número de Avisos", fontsize=12)
plt.tight_layout()
plt.show()
