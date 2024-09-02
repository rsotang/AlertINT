import pandas as pd
from openpyxl import load_workbook

# Suponiendo que ya tienes un DataFrame llamado df
df = pd.DataFrame({
    'Columna1': [1, 2, 3],
    'Columna2': ['A', 'B', 'C']
})

# Ruta del archivo de Excel
archivo_excel = 'prueba.xlsx'

# Cargar el libro de trabajo existente
libro = load_workbook(archivo_excel, keep_vba=True)

# Seleccionar la hoja de trabajo en la que quieres añadir los datos
hoja = libro['Hoja1']

# Encontrar la última fila con contenido en la hoja
ultima_fila = hoja.max_row

# Añadir las filas del DataFrame a partir de la última fila con contenido
for i, fila in df.iterrows():
    for j, valor in enumerate(fila):
        hoja.cell(row=ultima_fila + i + 1, column=j + 1, value=valor)

# Guardar los cambios en el archivo de Excel
libro.save(archivo_excel)

print("Datos añadidos exitosamente.")