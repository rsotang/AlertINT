
import os
import xml.etree.ElementTree as ET

import pandas as pd

#ESTA ES UNA VERSION MODIFICA DE import_XML_biplano.py CON EL FIN DE VERIFICAR SI FUNCIONA IGUAL DE BIEN PARA TODOS LOS EQUIPOS Y MÁS ADELANTE AÑADIR REDUNDANCIA Y CONTROL DE ERRORES AL SCRIPT COMPLEO


def parse_xml_to_df(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Crear una lista para almacenar los datos
    data_list = []

    # Verificar si se encontró <Query_Criteria>
    query_criteria = root.find('Query_Criteria')
    if query_criteria is not None:
        base_data = query_criteria.attrib
        #print("Query_Criteria encontrado:", base_data)

        # Recorrer cada <DoseInfo> y sus subelementos
        for dose_info in query_criteria.findall('DoseInfo'):
            dose_info_data = dose_info.attrib
            #print("DoseInfo encontrado:", dose_info_data)

            # Extraer <Observer_Context> asociado
            observer_context = dose_info.find('Observer_Context')
            if observer_context is not None:
                dose_info_data.update(observer_context.attrib)
                #print("Observer_Context encontrado:", observer_context.attrib)

            # Extraer todos los <CT_Accumulated_Dose_Data>
            for accumulated_dose in dose_info.findall('CT_Accumulated_Dose_Data'):
                accumulated_data = accumulated_dose.attrib
                #print("CT_Accumulated_Dose_Data encontrado:", accumulated_data)
                combined_data = {**base_data, **dose_info_data, **accumulated_data}
                data_list.append(combined_data)

            # Extraer todos los <CT_Acquisition>
            #for acquisition in dose_info.findall('CT_Acquisition'):
            #    acquisition_data = acquisition.attrib
                #print("CT_Acquisition encontrado:", acquisition_data)
            #    combined_data = {**base_data, **dose_info_data, **acquisition_data}
            #    data_list.append(combined_data)
    #Esta es la parte que contiene la información mecánica de la maquina y que ene este caso nos da un poco igual
    else:
        print("No se encontró <Query_Criteria> en", xml_file)

    # Convertir la lista de diccionarios a un DataFrame
    if data_list:
        df = pd.DataFrame(data_list)
    else:
        df = pd.DataFrame()  # DataFrame vacío en caso de no encontrar datos

    return df

def ImportXML(input_dir):
    # Leer y combinar todos los archivos XML en un solo DataFrame
    all_data = pd.DataFrame()

    for file in os.listdir(input_dir):
        if file.endswith('.xml'):
            file_path = os.path.join(input_dir, file)
            print("Procesando archivo:", file_path)
            df = parse_xml_to_df(file_path)
            all_data = pd.concat([all_data, df], ignore_index=True)

    return all_data
#Esta función esta para eliminar las unidades de los xmls y poder quedarnos solo con los numeros
def clean_and_convert_to_float(column):
    # Extrae solo la parte numérica antes de cualquier carácter no numérico y convierte a float
    return pd.to_numeric(column.str.extract(r'^(\d*\.?\d*)')[0], errors='coerce')
#############################################

def main():
    input_dir = 'Pruebas de Victor/Paciente prueba Alertint/XML SiemensHemoD'
    all_data = ImportXML(input_dir)
    
    print(all_data)

    if 'Total_Acquisition_Time' in all_data.columns:
        all_data['Total_Acquisition_Time'] = clean_and_convert_to_float(all_data['Total_Acquisition_Time'])
    else:
        all_data['Total_Acquisition_Time'] = 0

    if 'Total_Fluoro_Time' in all_data.columns:
        all_data['Total_Fluoro_Time'] = clean_and_convert_to_float(all_data['Total_Fluoro_Time'])
    else:
        all_data['Total_Fluoro_Time'] = 0

    all_data['Dose_Area_Product_Total'] = clean_and_convert_to_float(all_data['Dose_Area_Product_Total']) * 10000

    all_data['Dose_RP_Total'] = clean_and_convert_to_float(all_data['Dose_RP_Total'])

    # Crear el campo "Tiempo de intervención"
    all_data['Tiempo de intervención'] = (all_data['Total_Acquisition_Time'] + all_data['Total_Fluoro_Time']) / 60

    # Añadir campos adicionales y predefinir valores
    all_data['equipo'] = 'ArtisZee'
    all_data['servicio'] = 'ArtisZee'
    all_data['nombre paciente'] = ''
    all_data['Seguimiento'] = ''

    # Reordenar columnas según el orden especificado
    columns_order = [
        'equipo', 'servicio', 'PatientID', 'nombre paciente', 'SeriesDate', 
        'SeriesTime', 'StudyDescription', 'Dose_Area_Product_Total', 
        'Dose_RP_Total', 'Tiempo de intervención', 'Seguimiento'
    ]
    all_data = all_data.reindex(columns=columns_order)
    #print('punto1')
    #print(all_data)     


    all_data['Seguimiento'] = all_data['Dose_RP_Total'].apply(lambda x: 'SI' if x > 5 else 'NO')
    #print(all_data)

    # Guardar todos los datos procesados
        #all_data.to_csv('PacientesBiplano.csv', index=False)
    #all_data.to_excel('PacientesSiemensHemod.xlsx', index=False)
   
    
if __name__ == "__main__":
    main()





