# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:30:47 2020

@author: Victor
"""
import os
import xml.etree.ElementTree as ET



file_dir = os.getcwd()
print(file_dir)

for archivo in os.listdir(file_dir):

    if archivo.endswith('.xml'):
        tree=ET.parse(archivo, parser=None)
        nombre=os.path.splitext(archivo)[0]+".txt"
        tree.write(nombre,encoding ="UTF8", method="text")
