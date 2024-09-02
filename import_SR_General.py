import pydicom
import pandas as pd
import os


#ESTA ES UNA VERSION REPETIDA DEL SCRIPT SR_PHILLIPS.PY QUE ES EL ORIGINAL DONDE ESTÁN TODOS LOS COMENTARIOS

#De momento parece que para General y Phillips los campos de los que sacamos los datos coinciden, pero puede ser susceptible de error, asi que en caso de que no se importen bien los datos de una maquina solo un posible erro rpuede ser que hayan actualizado los campos del SR de esa maquina y que no lo coja bien el script.

def extraer_datos_dosis(archivo_dicom):
    ds = pydicom.dcmread(archivo_dicom)

    dosis_total = 0.0
    tiempo_total_intervencion = 0.0
    pda_total = 0.0
    tiempo_fluo = 0.0  #Son datos separados que no se juntán en ninguna etiqueta, 
    tiempo_adq = 0.0   #asi que los sumamos nosostros a mano

    # Navegar a través de los eventos de irradiación
    for item in ds.ContentSequence:
        if hasattr(item, 'ContentSequence'):
            for subitem in item.ContentSequence:
                # Extraer la dosis a punto de referencia
                if subitem.ConceptNameCodeSequence[0].CodeValue == '113725':  # Código NEMA para dosis a punto de referencia
                    dosis_referencia = float(subitem.MeasuredValueSequence[0].NumericValue)
                    dosis_total += dosis_referencia

                # Extraer el tiempo de fluoroscopia
                elif subitem.ConceptNameCodeSequence[0].CodeValue == '113730':  # Código NEMA para tiempo de fluoroscopia
                    tiempo_fluo = float(subitem.MeasuredValueSequence[0].NumericValue)

                # Extraer el tiempo de adquisición
                elif subitem.ConceptNameCodeSequence[0].CodeValue == '113855':  # Código NEMA para tiempo de adquisición
                    tiempo_adq = float(subitem.MeasuredValueSequence[0].NumericValue)

                # Extraer el producto dosis-área (PDA)
                elif subitem.ConceptNameCodeSequence[0].CodeValue == '113722':  # Código NEMA para producto dosis-área
                    pda = float(subitem.MeasuredValueSequence[0].NumericValue)
                    pda_total += pda

    # Calcular el tiempo total de intervención fuera del bucle
    tiempo_total_intervencion = tiempo_adq + tiempo_fluo 

    return dosis_total, tiempo_total_intervencion, pda_total

# Ruta de la carpeta que contiene los archivos SRDICOM
carpeta_srdicom = 'Pruebas de Victor/Paciente prueba Alertint/SR General'

# Lista para almacenar la información de cada archivo
datos_pacientes = []

# Iterar sobre los archivos en la carpeta
for archivo in os.listdir(carpeta_srdicom):
    if archivo.endswith('.dcm'):
        archivo_dicom = os.path.join(carpeta_srdicom, archivo)
        ds = pydicom.dcmread(archivo_dicom)

        # Extraer información adicional del paciente y estudio
        id_paciente = ds.PatientID
        nombre_paciente = ds.PatientName
        fecha_intervencion = ds.StudyDate
        hora_intervencion = ds.StudyTime
        descripcion_estudio = ds.StudyDescription if 'StudyDescription' in ds else 'N/A'

        # Extraer información de dosis, tiempo y PDA
        dosis_total, tiempo_total_intervencion, pda_total = extraer_datos_dosis(archivo_dicom)

 # Añadir los datos al DataFrame
        datos_pacientes.append({
            'Equipo': 'GE Vascular',
            'Servicio': 'Radiología',
            'ID Paciente': id_paciente,
            'Nombre Paciente': nombre_paciente,
            'Fecha Intervención': fecha_intervencion,
            'Hora Intervención': hora_intervencion,
            'Descripción del Estudio': descripcion_estudio,
            'PDA Total (Gy·cm²)': pda_total,
            'Dosis Total (Gy)': dosis_total,
            'Tiempo Total de Intervención (s)': tiempo_total_intervencion, 
            'Seguimiento': ''
        })

# Crear un DataFrame con los datos recolectados
df = pd.DataFrame(datos_pacientes)

df['Seguimiento'] = df['Dosis Total (Gy)'].apply(lambda x: 'SI' if x > 5 else 'NO')
# Mostrar el DataFrame
print(df)

# Opcional: guardar en un archivo CSV
df.to_csv('resultados_pacientes_General.csv', index=False)
#Hay que añadir el filtrado de datos y la exportación a excel